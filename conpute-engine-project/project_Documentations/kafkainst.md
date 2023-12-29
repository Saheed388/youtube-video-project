
Kafka Cluster Setup Documentation

--Create a VM Instance using Ubuntu
--Then avigate to your ssh

1. Update the package list:
sudo apt-get update
sudo apt-get install update 

2. Install default JDK:

sudo apt-get install default-jdk
java -version

3. Install wget:

sudo apt-get install wget
4. Create a new project directory and navigate into it:

--mkdir newproject
cd newproject

5. Download Kafka:

wget https://downloads.apache.org/kafka/3.5.0/kafka_2.12-3.5.0.tgz

6. Decompress the Kafka archive:

tar -xvzf kafka_2.12-3.5.0.tgz

7. check
ls -ltr
-it will return

total 104296
drwxr-xr-x 7 ajayiayodeji414 ajayiayodeji414      4096 Jun  5  2023 kafka_2.13-3.5.0
-rw-rw-r-- 1 ajayiayodeji414 ajayiayodeji414 106792776 Jun 13 10:29 kafka_2.13-3.5.0.tgz

7. Set Kafka home:
export KAFKA_HOME=/home/ajayiayodeji414/kafka/kafka_2.12-3.5.0

8. Configure Firewall Rules
Allow firewall rules:

gcloud compute firewall-rules create allow-all-ports \
--allow all \
--source-range 0.0.0.0/0 \
--target-tags kafka-project
Or navigate to the firewall rule configuration.

9. Copy Kafka server properties for multiple brokers:

cp ${KAFKA_HOME}/config/server.properties ${KAFKA_HOME}/config/server1.properties
cp ${KAFKA_HOME}/config/server.properties ${KAFKA_HOME}/config/server2.properties

10. Edit the configuration:

vim ${KAFKA_HOME}/config/server1.properties

After usining that we need to change some things file that will pop up
To make it editable 
-- qa
--To save esc 
:wq
--Uncomment 
listener
adverities.listener 
--change the host to vn 
external ip

11. To run the zookeer and the brooker
mkdir -p ${KAFKA_HOME}/logs
export KAFKA_HOME=/home/ajayiayodeji414/kafka/kafka_2.12-3.5.0

--Run the zookeeper
${KAFKA_HOME}/bin/zookeeper-server-start.sh ${KAFKA_HOME}/config/zookeeper.properties > ${KAFKA_HOME}/logs/zookeeper.log 2>&1 &

12. Run Kafka Brokers:

${KAFKA_HOME}/bin/kafka-server-start.sh ${KAFKA_HOME}/config/server.properties > ${KAFKA_HOME}/logs/broker1.log 2>&1 &

${KAFKA_HOME}/bin/kafka-server-start.sh ${KAFKA_HOME}/config/server.properties > ${KAFKA_HOME}/logs/broker2.log 2>&1 &

13. Create topic

${KAFKA_HOME}/bin/kafka-topics.sh --create --topic my1_topic --bootstrap-server 34.42.19.194:9092 --partitions 1 --replication-factor 1

producer
${KAFKA_HOME}/bin/kafka-console-producer.sh --topic my_topic --bootstrap-server 34.48.33.235:9092

consumer
${KAFKA_HOME}/bin/kafka-console-consumer.sh --topic my1_topic --bootstrap-server 34.42.19.194:9092
${KAFKA_HOME}/bin/kafka-console-consumer.sh --topic my_topic --bootstrap-server 34.42.19.194:9092 --group 1111

--To start an existing  kafka on on diffrent terminal

export KAFKA_HOME=/home/ajayiayodeji414/kafka/kafka_2.12-3.5.0

${KAFKA_HOME}/bin/zookeeper-server-start.sh ${KAFKA_HOME}/config/zookeeper.properties > ${KAFKA_HOME}/logs/zookeeper.log 2>&1 &

${KAFKA_HOME}/bin/kafka-server-start.sh ${KAFKA_HOME}/config/server.properties 

sudo chmod +x deploy.sh


--To delete the kafka

sudo rm -rf /opt/kafka
sudo rm -rf /var/lib/zookeeper
sudo systemctl daemon-reload
sudo apt-get remove --auto-remove kafka_2.13-3.5.0

--Delete foler terminal
rm -ri newproject



Install docker on terminal

sudo apt-get update
sudo apt-get install docker.io
docker --version
docker run hello-world
docker build -t spotify_image:tag .

docker run --name collect_spotify_container spotify_image:tag
