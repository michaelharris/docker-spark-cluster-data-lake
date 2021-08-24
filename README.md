# Spark Cluster with Docker & docker-compose

# General

Spark standalone cluster for testing/local environment, includes example configuration connection to Azure data lake. 

The Docker compose will create the following containers:

container|Exposed ports
---|---
spark-master|9090 7077
spark-worker-1|9091
spark-worker-2|9092

# Installation

The following steps will make you run your spark cluster's containers.

## Pre requisites

* Docker

* Docker compose

## Build the image


```sh
docker build -t cluster-apache-spark:3.0.2 .
```

## Run the docker-compose

The final step to create your test cluster will be to run the compose file:

```sh
docker-compose up -d
```

## Access your cluster

Just validate your cluster accesing the spark UI on each worker & master URL.

### Spark Master

http://localhost:9090/

### Spark Worker 1

http://localhost:9091/

### Spark Worker 2

http://localhost:9092/

## Submitting a job

From one of the workers (docker exec -it <container> bash)

```
 /opt/spark/bin/spark-submit --master spark://spark-master:7077 \
 --driver-memory 1G \
 --executor-memory 1G \
 --properties-file /opt/job-conf/datalake.properties \
 /opt/spark-apps/datalake.py
 ```