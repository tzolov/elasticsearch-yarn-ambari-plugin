# Ambari plugin for Elasticsearch on Yarn
Ambari plugin for Elasticsearch on YARN: https://www.elastic.co/guide/en/elasticsearch/hadoop/current/es-yarn.html

Supports PivotalHD 30, Hortonworks HDP2.2 and HDP2.3 (e.g. Ambari 1.7 to Ambari 2.1) Hadoop distributions. 

## How to build 
Clone the project locally
```
git clone https://github.com/tzolov/elasticsearch-yarn-ambari-plugin.git
```
Build All: installation tarball + RPMs for each supported Ambari stack 
```
cd elasticsearch-yarn-ambari-plugin
./gradlew clean dist -PbuildDir=target
```
Reuslt artefacts are generated in `target/distributions` folder
```
ls -la target/distributions/
drwxr-xr-x  6 tzoloc  720748206   204 Jul 24 15:02 .
drwxr-xr-x  4 tzoloc  720748206   136 Jul 24 15:02 ..
-rw-r--r--  1 tzoloc  720748206  3681 Jul 24 15:02 elasticsearch-yarn-ambari-plugin-0.1.11-1.tgz
-rw-r--r--  1 tzoloc  720748206  7891 Jul 24 15:02 elasticsearch-yarn-ambari-plugin-hdp22-0.1.11-1.noarch.rpm
-rw-r--r--  1 tzoloc  720748206  7891 Jul 24 15:02 elasticsearch-yarn-ambari-plugin-hdp23-0.1.11-1.noarch.rpm
-rw-r--r--  1 tzoloc  720748206  7892 Jul 24 15:02 elasticsearch-yarn-ambari-plugin-phd30-0.1.11-1.noarch.rpm
```
Alternatively you can use the Maven pom whcih is bearly a wrapper over the gradle build file. 
```
mvn clean package
```
Result is in `target/distributions`. 

## How to install the plugin
You can install the Ambari plugion either form the tarlball or RPM/YUM as explained below
#### 1. Install from tarball (`elasticsearch-yarn-ambari-plugin-xxx.tgz`).
Copy the tarball to your Ambari server and uncompress it under the desired Ambari stack folder:
```
/var/lib/ambari-server/resources/stacks/<STACK NAME>/<STACK VERSION>/services
```
Substitue the stack (name, version) with one of the supported pairs:

  Stack Name|Stack Version | Ambari Version
  --------|----------------|---
  PHD | 3.0 | 1.7
  HDP | 2.2 | 2.0.x
  HDP | 2.3 | 2.1.x

#### 2. Install from RPM
Copoy/download the RPM binary for the desired stack to your Ambari server.
Install the target rpms and restart Ambari Server. For example to install the pluting on HDP2.3:
```
sudo yum -y ./elasticsearch-yarn-ambari-plugin-hdp23-0.1.11-1.noarch.rpm
sudo /etc/init.d/ambari-server restart 
```
#### 3. Install from pulblic YUM repository
//TODO 

## How to Deploy Elasticserach YARN cluster using the Ambari UI

