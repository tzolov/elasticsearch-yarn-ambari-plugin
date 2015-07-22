#!/usr/bin/python
import params
import os

# ES user
es_user = 'elastic'

# ES YARN jar path
es_jar_path = '/opt/es/elasticsearch-yarn.jar'

es_hdfs_upload_dir = '/apps/elasticsearch/'

if os.path.isfile(params.es_user_file):
  with open(params.es_user_file, 'r') as f:
      es_user = f.readline().strip()
      
if os.path.isfile(params.es_jar_path_file):
  with open(params.es_jar_path_file, 'r') as f:
      es_jar_path = f.readline().strip()
      
if os.path.isfile(params.es_hdfs_upload_dir_file):
  with open(params.es_hdfs_upload_dir_file, 'r') as f:
      es_hdfs_upload_dir = f.readline().strip()      