#!/usr/bin/python
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

import params
import os

# ES user
es_user = 'elastic'

# ES YARN jar path: default value
es_jar_path = '/opt/es/elasticsearch-yarn.jar'

# ES HDFS upload directory: default value
es_hdfs_upload_dir = '/apps/elasticsearch/'

if os.path.isfile(params.es_user_file):
	with open(params.es_user_file, 'r') as f:
		es_user = f.readline().strip()

# Override the ES jar path with the value set when the service was started
if os.path.isfile(params.es_jar_path_file):
	with open(params.es_jar_path_file, 'r') as f:
		es_jar_path = f.readline().strip()

# Override the ES jar path with the value set when the service was started
if os.path.isfile(params.es_hdfs_upload_dir_file):
	with open(params.es_hdfs_upload_dir_file, 'r') as f:
		es_hdfs_upload_dir = f.readline().strip()      