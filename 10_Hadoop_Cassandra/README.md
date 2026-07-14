# Hybrid Big Data Processing using Apache Hadoop and Apache Cassandra

A hybrid Big Data analytics project demonstrating the integration of **Apache Hadoop** for batch processing and **Apache Cassandra** for real-time NoSQL data storage in a **WSL (Windows Subsystem for Linux)** environment.

---

## Project Overview

This project combines Hadoop Streaming MapReduce and Apache Cassandra to process music streaming data. Real-time records are stored in Cassandra, while large batch datasets are processed using Hadoop MapReduce. The analytical results are then loaded back into Cassandra for efficient querying.

---

## Objectives

- Install Apache Cassandra using Docker in WSL.
- Create Cassandra keyspace and tables.
- Generate batch music streaming data.
- Upload data into Hadoop HDFS.
- Perform batch analytics using Hadoop Streaming MapReduce.
- Load analytical results into Cassandra.
- Execute Cassandra queries.
- Understand hybrid Big Data architecture.

---

## Technologies Used

- Apache Hadoop
- Hadoop Streaming
- Apache Cassandra
- Docker
- Python
- HDFS
- WSL (Ubuntu)

---

## Project Structure

```
hadoop-cassandra-exercise/
│── docker-compose.yml
│── README.md
│
├── data/
├── scripts/
│   ├── cassandra_schema.cql
│   ├── load_realtime_data.cql
│   ├── generate_batch_data.py
│   ├── load_hadoop_results.py
│   ├── mapper_daily_aggregate.py
│   ├── reducer_daily_aggregate.py
│   ├── mapper_top_songs.py
│   └── reducer_top_songs.py
│
├── jobs/
└── output/
```

---

## Cassandra Tables

- current_top_songs
- user_listening_history
- hourly_stats
- user_sessions
- daily_aggregates
- top_songs_daily
- user_recommendations

---

## Features

- Dockerized Apache Cassandra
- Batch data generation using Python
- Hadoop HDFS integration
- Hadoop Streaming MapReduce
- Daily aggregation analysis
- Top songs analysis
- Loading analytics into Cassandra
- Querying processed data

---

## Workflow

1. Start Cassandra using Docker Compose.
2. Create Cassandra schema.
3. Load real-time music streaming data.
4. Generate batch CSV dataset.
5. Upload dataset to HDFS.
6. Execute Hadoop Streaming jobs.
7. Generate analytical outputs.
8. Load Hadoop results into Cassandra.
9. Query Cassandra tables.

---

## Main Commands

Start Cassandra

```bash
docker compose up -d
```

Connect to Cassandra

```bash
docker exec -it cassandra cqlsh
```

Execute Schema

```bash
docker exec -i cassandra cqlsh < scripts/cassandra_schema.cql
```

Generate Batch Data

```bash
python3 scripts/generate_batch_data.py
```

Upload Data to HDFS

```bash
hdfs dfs -put data/batch_plays.csv /user/$USER/analytics/input/
```

Run Hadoop Streaming

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar
```

Load Results

```bash
python3 scripts/load_hadoop_results.py
```

---

## Screenshots

- Cassandra Container Running
- Cassandra Connection
- HDFS Upload
- Hadoop Streaming Output
- Cassandra Query Results

---

## Learning Outcomes

- Apache Hadoop Streaming
- Apache Cassandra Data Modeling
- HDFS Operations
- Docker Container Management
- Hybrid Big Data Processing
- Batch and Real-Time Analytics

---

## Conclusion

This project demonstrates a hybrid Big Data pipeline by integrating Apache Hadoop and Apache Cassandra. Hadoop efficiently processes large-scale batch datasets using MapReduce, while Cassandra stores and serves real-time analytical results with high performance. The project provides hands-on experience with modern Big Data technologies and scalable data processing workflows.
