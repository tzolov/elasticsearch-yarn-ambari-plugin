# Uninstall Elasticsearch YARN plugin

#### Unistall and clean
```
curl -u admin:admin -i -H 'X-Requested-By: ambari' -X PUT -d '{"RequestInfo": {"context" :"Stop Elasticsearch-YARN via REST"}, "Body": {"ServiceInfo": {"state": "INSTALLED"}}}' http://ambari.localdomain:8080/api/v1/clusters/PHD30C1/services/ELASTICSEARCH_YARN

curl --user admin:admin  -H 'X-Requested-By:mycompany' -X DELETE http://ambari.localdomain:8080/api/v1/clusters/PHD30C1/services/ELASTICSEARCH_YARN

sudo /etc/init.d/ambari-server stop
sudo rm -Rf /var/lib/ambari-agent/cache/stacks/PHD/3.0/services/ELASTICSEARCH_YARN

hadoop jar /opt/es/elasticsearch-yarn.jar -stop
hadoop jar /opt/es/elasticsearch-yarn.jar -status

sudo rm -Rf /opt/es
sudo userdel elastic
sudo rm -Rf /home/elastic

sudo yum -y remove elasticsearch-yarn-ambari-plugin-phd30
sudo yum -y remove elasticsearch-yarn-ambari-plugin-hdp23
sudo rm /vagrant/elasticsearch-yarn-ambari-plugin-*.rpm
sudo rm -Rf /var/lib/ambari-server/resources/stacks/HDP/2.3/services/ELASTICSEARCH_YARN
sudo rm -Rf /var/lib/ambari-server/resources/stacks/PHD/3.0/services/ELASTICSEARCH_YARN
sudo rm /var/lib/ambari-agent/data/ELASTICSEARCH_YARN_MASTER_config.json

sudo su -u hdfs hdfs dfs -rm -R /apps
```

#### Reinstall 
```
[ -f /etc/yum.repos.d/bintray-big-data-rpm.repo ] || sudo wget https://bintray.com/big-data/rpm/rpm -O /etc/yum.repos.d/bintray-big-data-rpm.repo
sudo yum -y info elastic*

sudo yum -y install elasticsearch-yarn-ambari-plugin-hdp23

sudo /etc/init.d/ambari-server restart
```