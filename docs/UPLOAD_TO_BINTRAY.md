# Upload the RPMs to the Bintray Big-Data YUM repo

1. Set the Bintray `big-data` API key in `BINTRAY_BIGDATA_KEY` environment variable
```
source ~/.bash_profile
```

2. Build the RPMs (`build/distributions`) and upload them to the Bintray YUM repository
```
./gradlew clean dist bintrayUpload
```

3. Open the [Bintray big-data/rpm/elasticsearch-yarn-ambari-plugin](https://bintray.com/big-data/rpm/elasticsearch-yarn-ambari-plugin/view) repository and publish the RPMs
