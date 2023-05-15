sudo docker run -d \
           -P \
           --name=alluxio-master \
           -v ufs:/opt/alluxio/underFSStorage \
           -e ALLUXIO_JAVA_OPTS="-Dalluxio.master.hostname=alluxio-master" \
           -e ALLUXIO_MASTER_WEBUI_RESTSERVICE_ENABLED=true \
           alluxio/alluxio master

           #--net=host \
#alluxio.master.hostname, configure zookeeper with alluxio.zookeeper.enabled=true and alluxio.zookeeper.address=[comma-separated zookeeper master addresses]
