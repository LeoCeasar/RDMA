sudo docker run -d \
           --net=host \
           --name=alluxio-worker \
           --shm-size=50G \
           -v /:/opt/alluxio/underFSStorage \
           -e ALLUXIO_JAVA_OPTS="-Dalluxio.worker.memory.size=50G -Dalluxio.master.hostname=alluxio-master" \
           alluxio/alluxio worker
