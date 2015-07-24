#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from resource_management import *

class ElasticSearchMaster(Script):

	def es_user_exists(self, user):
		import pwd
		
		try:
		   pwd.getpwnam(user)
		   return True
		except KeyError:
		   return False

	def create_es_user(self):
		import crypt
		import params		
		
		Group(params.es_group)
		User(params.es_user, gid=params.es_group, password=crypt.crypt(params.es_password, 'salt'), groups=[params.es_group], ignore_failures=True)		
			  
	def create_es_hdfs_user(self):
		import params
		
		ExecuteHadoop(format('fs -mkdir -p /user/{es_user}'), user='hdfs', conf_dir=params.hadoop_conf_dir, ignore_failures=True)
		ExecuteHadoop(format('fs -chown {es_user} /user/{es_user}'), user='hdfs', conf_dir=params.hadoop_conf_dir)
		ExecuteHadoop(format('fs -chgrp {es_user} /user/{es_user}'), user='hdfs', conf_dir=params.hadoop_conf_dir)
		
	def create_es_hdfs_upload_dir(self):
		import params
		
		ExecuteHadoop(format('fs -mkdir -p {es_hdfs_upload_dir}'), user='hdfs', conf_dir=params.hadoop_conf_dir, ignore_failures=True)
		ExecuteHadoop(format('fs -chown {es_user} {es_hdfs_upload_dir}'), user='hdfs', conf_dir=params.hadoop_conf_dir)
		ExecuteHadoop(format('fs -chgrp {es_user} {es_hdfs_upload_dir}'), user='hdfs', conf_dir=params.hadoop_conf_dir)

	def store_status_properties(self):
		import params

		with open(params.es_user_file, "w") as es_user_file:
			es_user_file.write("%s\n" % params.es_user)
		with open(params.es_jar_path_file, "w") as es_jar_path_file:
			es_jar_path_file.write("%s\n" % params.es_jar_path)
		with open(params.es_hdfs_upload_dir_file, "w") as es_hdfs_upload_dir_file:
			es_hdfs_upload_dir_file.write("%s\n" % params.es_hdfs_upload_dir)	
 
	def install(self, env):
		import params
		
		env.set_params(params)

		self.configure(env)
		
		self.create_es_hdfs_upload_dir()
				
		Execute(format('hadoop jar {es_jar_path} -download-es hdfs.upload.dir={es_hdfs_upload_dir} download.local.dir={es_download_local_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)
		Execute(format('hadoop jar {es_jar_path} -install-es hdfs.upload.dir={es_hdfs_upload_dir} download.local.dir={es_download_local_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)
		Execute(format('hadoop jar {es_jar_path} -install hdfs.upload.dir={es_hdfs_upload_dir} download.local.dir={es_download_local_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)
		
		# Store the properties required by STATUS phase. Note that the STATUS phase has no access to the Script.get_config()   
		self.store_status_properties()

	def configure(self, env):
		import os
		import params
		import urllib

		env.set_params(params)

		if not self.es_user_exists(params.es_user):
			self.create_es_user()
			self.create_es_hdfs_user()		
		
		if not (os.path.exists(params.es_jar_path) and os.path.isfile(params.es_jar_path)) :
			es_jar_dir = os.path.dirname(os.path.abspath(params.es_jar_path))
			Directory(es_jar_dir, owner=params.es_user, group=params.es_group, recursive=True)						
			print "Downloading ES YARN jar from: %s to: %s" % (params.es_jar_download_url, params.es_jar_path)
			geodeTarball = urllib.URLopener()
			geodeTarball.retrieve(params.es_jar_download_url, params.es_jar_path)	
        
        	File(format("/home/{es_user}/elasticsearch.properties"), owner=params.es_user, group=params.es_group, content=params.es_load_config_file)
        
	def start(self, env):
		import params
		env.set_params(params)
		self.configure(env)
		
		Execute(format('hadoop jar {es_jar_path} -start containers={es_yarn_container_count} container.mem={es_yarn_container_mem} container.vcores={es_yarn_container_vcores} container.priority={es_yarn_container_priority} hdfs.upload.dir={es_hdfs_upload_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), 
			user=params.es_user, logoutput=True, timeout=300)

	def stop(self, env):
		import params
		env.set_params(params)
		
		Execute(format('hadoop jar {es_jar_path} -stop hdfs.upload.dir={es_hdfs_upload_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)

	def status(self, env):
		import status_params
		env.set_params(status_params)
		
		Execute(format('hadoop jar {es_jar_path} -status hdfs.upload.dir={es_hdfs_upload_dir} loadConfig=/home/{es_user}/elasticsearch.properties| grep RUNNING'), user=status_params.es_user, logoutput=True, timeout=300)

if __name__ == '__main__':
	ElasticSearchMaster().execute()
