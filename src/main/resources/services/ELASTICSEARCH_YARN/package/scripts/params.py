#!/usr/bin/python

from resource_management import *

config = Script.get_config()

# common configs
java64_home = config['hostLevelParams']['java_home']

# ES user
es_version = config['configurations']['elasticsearch-site']['es.version']

# ES user
es_user = config['configurations']['elasticsearch-site']['es.user']

# ES group
es_group = config['configurations']['elasticsearch-site']['es.group']

# ES user password
es_password = config['configurations']['elasticsearch-site']['es.user.password']

# ES YARN jar path
es_jar_path = config['configurations']['elasticsearch-site']['es.jar.path']

# ES YARN jar download URL
es_jar_download_url = config['configurations']['elasticsearch-site']['es.jar.download.url']

# Local dir to store downloaded ES
es_download_local_dir = config['configurations']['elasticsearch-site']['download.local.dir']

# Number of YARN containers to use in the ES cluster.
es_yarn_container_count = config['configurations']['elasticsearch-site']['es.yarn.container.count']

# Mem for each YARN container.
es_yarn_container_mem = config['configurations']['elasticsearch-site']['es.yarn.container.mem']

# CPUs for each YARN container.
es_yarn_container_vcores = config['configurations']['elasticsearch-site']['es.yarn.container.vcores']

# YARN queue priority for each container.
es_yarn_container_priority = config['configurations']['elasticsearch-site']['es.yarn.container.priority']

# Hadoop config location
hadoop_conf_dir = "/etc/hadoop/conf"

# ES HDFS upload folder
es_hdfs_upload_dir = config['configurations']['elasticsearch-site']['es.hdfs.upload.dir']

# Used to exchanged info with the status method
es_user_file = "/opt/es/es_user.txt"
es_jar_path_file = "/opt/es/es_jar_path.txt"
es_hdfs_upload_dir_file = "/opt/es/es_hdfs_upload_dir.txt"