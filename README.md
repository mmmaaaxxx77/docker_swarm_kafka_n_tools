# Deploy Kafka with kafka-manager in Docker Swarm
1. Using Docker Swarm to deploy Kafka Cluster and kafka-manager.
2. Three Kafka nodes cluster and kafka-manager UI.
3. One zookeeper node, but you can start multiple nodes if you want.

## Start Kafka Cluster
```shell script
$ docker stack deploy -c docker-compose.yml kafka
```

## kafka-manager UI
http://{domain or ip}:9000

## Kafka Commands
Here are some useful kafka commands.

### Show consumer list
```shell script
$ ./kafka-consumer-groups.sh --new-consumer --bootstrap-server ip:9092 --list
```

### Show group now offset
```shell script
$ ./kafka-consumer-groups.sh --new-consumer --bootstrap-server ip:9092 --describe --group groupName
```  

### Reset group offset
```shell script
$ ./kafka-consumer-groups.sh --bootstrap-server ip:9092 --group groupName --reset-offsets --to-offset 0 --topic topicName --execute
```

### Delete comsumer
```shell script
$ ./kafka-consumer-groups.sh --bootstrap-server ip:9092 --delete --group <group-name>
```

### Get the earliest offset still in a topic
```shell script
$ ./kafka-run-class.sh kafka.tools.GetOffsetShell --broker-list 104.199.243.52:9092 --topic topic1 --time -2
```


## Reference
https://gist.github.com/ursuad/e5b8542024a15e4db601f34906b30bb5