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

	def hdfs_path_exists(self, hdfs_path):
		import params
		try:
			Execute(format('hadoop fs -test -e {hdfs_path}'), user=params.es_user, logoutput=True, timeout=300)
			return True
		except:
			return False
				
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
		
		File(format("{es_user_file}"), owner=params.es_user, group=params.es_group, content=params.es_user)
		File(format("{es_jar_path_file}"), owner=params.es_user, group=params.es_group, content=params.es_jar_path)
		File(format("{es_hdfs_upload_dir_file}"), owner=params.es_user, group=params.es_group, content=params.es_hdfs_upload_dir)
 	
	def install(self, env):
		import params
		env.set_params(params)
	
	def configure(self, env):
		import os
		import params
		import urllib
		
		env.set_params(params)
		
		if not self.es_user_exists(params.es_user):
			self.create_es_user()
		
		if not (os.path.exists(params.es_jar_path) and os.path.isfile(params.es_jar_path)) :
			es_jar_dir = os.path.dirname(os.path.abspath(params.es_jar_path))
			Directory(es_jar_dir, owner=params.es_user, group=params.es_group, recursive=True)
			print "Downloading ES YARN jar from: %s to: %s" % (params.es_jar_download_url, params.es_jar_path)
			geodeTarball = urllib.URLopener()
			geodeTarball.retrieve(params.es_jar_download_url, params.es_jar_path)
			
			File(format("/home/{es_user}/elasticsearch.properties"), owner=params.es_user, group=params.es_group, content=params.es_load_config_file)
		
		if not self.hdfs_path_exists("/user/" + params.es_user) :
			self.create_es_hdfs_user()
		
		if not self.hdfs_path_exists(params.es_hdfs_upload_dir) :
			self.create_es_hdfs_upload_dir()
			Execute(format('hadoop jar {es_jar_path} -download-es hdfs.upload.dir={es_hdfs_upload_dir} download.local.dir={es_download_local_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)
			Execute(format('hadoop jar {es_jar_path} -install-es hdfs.upload.dir={es_hdfs_upload_dir} download.local.dir={es_download_local_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)
			Execute(format('hadoop jar {es_jar_path} -install hdfs.upload.dir={es_hdfs_upload_dir} download.local.dir={es_download_local_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)
		
		# Store the properties required by STATUS phase. Note that the STATUS phase has no access to the Script.get_config()
		self.store_status_properties()
	
	# Called by Ambari on ES service start
	def start(self, env):
		import params
		env.set_params(params)
		
		# Call the configure method on start to make sure any re-configurations would be applied.   
		self.configure(env)
		
		Execute(format('hadoop jar {es_jar_path} -start containers={es_yarn_container_count} container.mem={es_yarn_container_mem} container.vcores={es_yarn_container_vcores} container.priority={es_yarn_container_priority} hdfs.upload.dir={es_hdfs_upload_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'),
			user=params.es_user, logoutput=True, timeout=300)
	
	# Called by Ambari on ES service stop
	def stop(self, env):
		import params
		env.set_params(params)
		
		Execute(format('hadoop jar {es_jar_path} -stop hdfs.upload.dir={es_hdfs_upload_dir} es.version={es_version} loadConfig=/home/{es_user}/elasticsearch.properties'), user=params.es_user, logoutput=True, timeout=300)
	
	# Warning: Ambari doesn't share the configuration parameters (e.g. elasticsearch-site.xml) in the status phase. To access some of those properties one has store them during the 'START' phase in shared store with the 'STATUS' phase   
	def status(self, env):
		import status_params
		env.set_params(status_params)
		
		Execute(format('hadoop jar {es_jar_path} -status hdfs.upload.dir={es_hdfs_upload_dir} loadConfig=/home/{es_user}/elasticsearch.properties| grep RUNNING'), user=status_params.es_user, logoutput=True, timeout=300)

if __name__ == '__main__':
	ElasticSearchMaster().execute()
