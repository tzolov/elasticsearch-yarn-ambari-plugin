# Deploy Elasticsearch YARN Cluster


#### Open the Ambari UI
![HDP2.3 Cluster](1_HDP23_CLUSTER_VIEW.png)

#### Select `Actions` -> `Add Services` menu
![AddService](2_AMBARI_ADD_SERVICE.png)

#### Select the `Elasticsearch YARN` service and press `Next`
![Select YARN](3_SELECT_ES_YARN_TO_INSTALL.png)

#### Select where to deploy the `Elasticsearch YARN Master` and press `Next`
![Select Master](4_SELECT_MASTER_HOST.png)

#### Edit the configuration and press `Next`
![Configurationr](5_SET_CONFIGURATION.png)

#### Wait the installation to complete and press `Next` 
![Installation progress](6_ES_INSTALL_PROGRESS.png)`
![Installation done](7_ES_INSTALL_DONE.png)

#### Check the Elasticsearch status.
![Check status](8_CHECK_ES_STATUS.png)

#### From the YARN UI check the ES AM and Containers statuses. 
![YARN UI](9_OPEN_YARN_UI.png)
![YARN AM](10_ES_YARN_MASTER.png)
![YARN Containers](11_ES_YARN_CONTAINERS.png)

#### Finally use Elasticsearch API to check the healt of the cluster
![Check status](13_ES_HEALT.png)
![Check status](12_ES_NODES.png)



`Elasticsearch on YARN` usage guide: https://www.elastic.co/guide/en/elasticsearch/hadoop/current/ey-usage.html
