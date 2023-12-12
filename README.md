# Kafka-Spark-Integration
This project  will  allows real-time visualization of the status of bike stations with the number of available bikes. This enables users to target stations for bike pickup or drop-off, as well as providing insights for station managers.

## Technologies Used

- Apache Kafka: 3.6.0
- Apache Spark: 3.2.4
- Elasticsearch: 8.8.2
- kibana : 8.8.2
- Scala: 2.12.15

## Project Architecture

![Project Architecture](images/Screenshot%20from%202023-11-23%2017-46-31.png)

Description of the project architecture:

- **Kafka**: Used for real-time streaming of bike station data using availabe API.
- **Spark**: Processes and analyzes the streaming data from Kafka for real-time insights.
- **Elasticsearch**: Stores the processed data for efficient querying and visualization.
![kibana](images/Screenshot%20from%202023-11-23%2017-44-02.png)
##Visualization
Inspect the evolution of availble bikes in 3 different cities in real time :
![numbre of available bikes ](images/Screenshot%20from%202023-12-08%2020-35-33.png)
A capture showing bruxelle city map with available bikes stands .
![example of map visualisation  ](images/Screenshot%20from%202023-12-08%2021-11-15.png)
# Running the consumer 
1. Start Kafka and Zookeeper:

    ```sh
    sudo systemctl start kafka
    sudo systemctl start zookeeper
    ```

2. Start Elasticsearch:

    ```sh
    elasticsearch
    ```

3. Run the Python script to index data in Elasticsearch:

    ```sh
    python3 index.py
    ```

4. Start the Kafka producer:

    ```sh
    python3 kafka.py
    ```

5. Start the consumer:

    ```sh
    ./commands.sh
    ```
  
# Store Historical Data in a Hive Table

This section demonstrates the integration of PySpark with Hive for processing and storing historical data. The following dependencies have been used:

- **Hadoop**: 2.10.2
- **Hive**: 2.3.9

## Running the Consumer

To run the consumer, follow these steps:

1. Add the following line to the `packages` section in the `commands.sh` file:

    ```sh
    org.apache.spark:spark-hive_2.12:3.2.4
    ```

2. Add the following line to the `conf` section in the `commands.sh` file:

    ```sh
    "org.apache.spark:spark-hive_2.12:3.2.4"
    ```

3. Ensure that the Hadoop cluster is running:

    ```sh
    ./sbin/start-all.sh
    ```

4. Ensure that the Hive service metastore is running:

    ```sh
    hive --service metastore
    ```

Now you are ready to run the consumer and store historical data in the Hive table.
