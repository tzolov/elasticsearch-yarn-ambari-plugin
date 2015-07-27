
# Deploy Elasticsearch YARN using the Ambari Blueprint API

Create a new (or edit existing such) Ambari blueprint and host mapping files.

##### 1. Blueprint 
 
Add the `elasticsearch-site` element to the blueprint `configuration` section

```
{  
 "elasticsearch-site": {
 "es.hdfs.upload.dir": "/apps/elasticsearch/",
 "es.yarn.container.count": "4",
 "es.yarn.container.mem": "1024",
 "download.local.dir": "./downloads/",
 "es.jar.download.url": "https://oss.sonatype.org/content/repositories/snapshots/org/elasticsearch/elasticsearch-yarn/2.2.0.BUILD-SNAPSHOT/elasticsearch-yarn-2.2.0.BUILD-20150722.024358-29.jar",

 "es.load.config": " env.ES_USE_GC_LOGGING=true env.PROP=someValue",
 "es.jar.path": "/opt/es/elasticsearch-yarn.jar",
 "es.user": "elastic",
 "es.version": "1.7.0",
 "es.group": "elastic",
 "es.yarn.container.priority": "-1",
 "es.yarn.container.vcores": "1"
}	  
```
Note that you can skip some properties and they will be initialized with the default values. 


Add the `ELASTICSEARCH_YARN_MASTER` component to one of blueprint's host_group: 

```
 "host_groups" : [
    {
      "name" : "management_masters",
      "configurations" : [ ],
      "components" : [
        ...
        
		{"name" : "ELASTICSEARCH_YARN_MASTER"},
		...
		        
      ],
      "cardinality" : "1+"
    },  
```

#### 3. Use the Ambari REST API to install the blue print and create cluster
Install the Blueprint
```
```

