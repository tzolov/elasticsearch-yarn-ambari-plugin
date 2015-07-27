# Ambari plugin for Elasticsearch on Yarn
Ambari plugin for Elasticsearch on YARN: https://www.elastic.co/guide/en/elasticsearch/hadoop/current/es-yarn.html
Plugin supports the PivotalHD30, Hortonworks HDP2.2 and HDP2.3 Hadoop distributions. The support spread for Ambari 1.7 to 2.1. 
## Quick Start
Adds the big-data YUM repo to your CentOS/RedHad system, install the plugin and restart Ambari server:
```
sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
sudo yum -y install elasticsearch-yarn-ambari-plugin-hdp23
sudo /etc/init.d/ambari-server restart 
```
_For HDP2.2 and PHD3.0 install `elasticsearch-yarn-ambari-plugin-hdp22` or `elasticsearch-yarn-ambari-plugin-phd30` instead._

Then follow the [Ambari Wizard](docs/README.md) guidelines to deploy an Elasticsearch on YARN cluster.

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

## How to install the plugin [ ![Download](https://api.bintray.com/packages/big-data/rpm/elasticsearch-yarn-ambari-plugin/images/download.svg) ](https://bintray.com/big-data/rpm/elasticsearch-yarn-ambari-plugin/_latestVersion)
You can install the Ambari plugion either form the tarlball or RPM/YUM as explained below
#### 1. From tarball package
Uncompress the tarball (`elasticsearch-yarn-ambari-plugin-xxx.tgz`) on the Ambari server node,  under the desired Ambari stack folder:
```
/var/lib/ambari-server/resources/stacks/<STACK NAME>/<STACK VERSION>/services
```
Substitue the stack (name, version) values with one from the supported stacks:

  Stack Name|Stack Version | Ambari Version
  --------|----------------|---
  PHD | 3.0 | 1.7
  HDP | 2.2 | 2.0.x
  HDP | 2.3 | 2.1.x

#### 2. From RPM file
Copoy/download the RPM binary for the desired stack to your Ambari server.
Install the target rpms and restart Ambari Server. For example to install the pluting on HDP2.3:
```
sudo yum -y ./elasticsearch-yarn-ambari-plugin-hdp23-0.1.11-1.noarch.rpm
sudo /etc/init.d/ambari-server restart 
```
#### 3. From public YUM repository
Adds the big-data YUM repo to your CentOS/RedHad system, install the plugin and restart Ambari server:
```
sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
sudo yum -y install elasticsearch-yarn-ambari-plugin-hdp23
sudo /etc/init.d/ambari-server restart 
```
_For HDP2.2 and PHD3.0 install `elasticsearch-yarn-ambari-plugin-hdp22` or `elasticsearch-yarn-ambari-plugin-phd30` instead._

## How to Deploy Elasticserach on YARN cluster using the Ambari Wizard 
1. Login to Ambari server
2. Open the `Services` view and click on `Actions`/`+Add Services` button.
3. Select the `Elasticsearch YARN` service from the list and press `Next`.
4. Select a host for the Elasticsearch Master component and press `Next`. Open the elasticsearch-site.xml configuration panel. By default the plugin checks if `es.jar.path` contains a valid ES YARN jar. If the jar is not available the plugin will use `es.jar.download.url` to download it. You can change the download URL or provide the jar locally (setting the `es.jar.path`). 
5. Press Next to finish the deployment.
For additional info follow the [Ambari Wizard](docs/README.md) instrucitons.

