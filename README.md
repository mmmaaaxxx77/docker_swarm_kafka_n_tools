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
