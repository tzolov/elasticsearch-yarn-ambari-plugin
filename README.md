# Ambari plugin for Elasticsearch on Yarn
Ambari plugin for Elasticsearch on YARN: https://www.elastic.co/guide/en/elasticsearch/hadoop/current/es-yarn.html
Plugin supports the PivotalHD30, Hortonworks HDP2.2 and HDP2.3 Hadoop distributions. The support spread for Ambari 1.7 to 2.1. 
## Quick Start
Adds the big-data YUM repo to your CentOS/RedHad system:
```
sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
```
Run this to install the plugin on HDP 2.3:
```
sudo yum -y install elasticsearch-yarn-ambari-plugin-hdp23
```
_For HDP2.2 install `elasticsearch-yarn-ambari-plugin-hdp22` and for PHD3.0 install `elasticsearch-yarn-ambari-plugin-phd30` instead._

Then use the [Ambari Wizard](docs/README.md) guidelines to deploy an Elasticsearch on YARN cluster.

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

Run the following to get a generated .repo file:
```
sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
```
or create a `bintray-big-data-rpm.repo` file in the `/etc/yum.repos.d/` dir with this content:
```
[bintraybintray-big-data-rpm]
name=bintray-big-data-rpm
baseurl=https://dl.bintray.com/big-data/rpm
gpgcheck=0
enabled=1 
```
Use `sudo yum info elasticsearch-yarn-ambari-plugin-*` to check the available plugin versions. For example to install the plugin for the HDP2.3 stack run:
```
sudo yum -y install elasticsearch-yarn-ambari-plugin-hdp23
```

## How to Deploy Elasticserach YARN cluster using the Ambari UI
Use the [Ambari Wizard](docs/README.md) to deploy an Elasticsearch on YARN cluster.
