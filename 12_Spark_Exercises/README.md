# Spark Exercises

This repository contains Apache Spark exercises and Big Data projects developed as part of the Big Data Analytics laboratory. The exercises demonstrate fundamental and advanced concepts of Apache Spark, while the projects showcase practical implementations of real-time data processing and optimization techniques.

---

## Technologies Used

- Apache Spark 4.1.2
- PySpark
- Apache Kafka (KRaft Mode)
- Apache Cassandra
- Hadoop HDFS
- Hadoop Streaming
- Python 3
- Java (JDK)
- WSL (Ubuntu)
- Spark Structured Streaming

---

# Exercises

## Exercise 1 – Spark Basics

- Creating Spark Session
- Reading CSV files
- Data analysis using DataFrames
- Aggregations and filtering

---

## Exercise 2 – DataFrame Operations

- DataFrame creation
- Filtering
- Sorting
- Group By
- Aggregations
- Column operations

---

## Exercise 3 – RDD Transformations and Actions

- RDD creation
- Map
- Filter
- FlatMap
- ReduceByKey
- Collect
- Count
- Save output

---

## Exercise 4 – Spark SQL

- Creating temporary views
- SQL queries
- Joins
- Aggregations
- Sorting
- SQL functions

---

## Exercise 5 – Streaming Analytics

- Structured Streaming
- Apache Kafka Integration
- Window Operations
- Watermarking
- Real-Time Analytics
- Rolling Aggregations

---

## Exercise 6 – Machine Learning Pipeline

- Feature Engineering
- Data Preprocessing
- ML Pipeline
- Model Training
- Predictions
- Evaluation

---

## Exercise 7 – Graph Processing

- Graph Analytics
- Vertices
- Edges
- Connected Components
- Shortest Paths
- Graph Operations

---

## Exercise 8 – Performance Tuning

- Partitioning
- Caching
- Persisting
- Memory Optimization
- Execution Optimization

---

## Exercise 9 – Optimization Techniques

- Repartition
- Coalesce
- Broadcast Join
- Cache
- Persist
- Adaptive Query Execution (AQE)
- Shuffle Partition Tuning
- Data Skew Handling

---

## Exercise 10 – Spark Project

- End-to-End Big Data Application
- Data Processing
- Analytics
- Reporting
- Performance Optimization

---

# Projects

## Project 1

A complete Big Data application demonstrating data ingestion, processing, analysis, and reporting using Apache Spark and the Hadoop ecosystem.

### Features

- Data Processing
- Data Cleaning
- Analytics
- Performance Optimization
- Result Generation

---

## Project 2

A real-world Big Data project integrating multiple technologies for scalable data processing and analytics.

### Features

- Apache Spark
- Kafka Streaming
- Cassandra Integration
- Hadoop HDFS
- Real-Time Analytics
- Big Data Pipeline

---

# How to Run

Clone the repository:

```bash
git clone https://github.com/mahisatani21/big-data-analytics.git
```

Move into the repository:

```bash
cd big-data-analytics
```

Navigate to the required exercise:

```bash
cd 12_Spark_Exercises/Exercise5
```

Activate the virtual environment (if applicable):

```bash
source venv/bin/activate
```

Run a Spark program:

```bash
python filename.py
```

For Structured Streaming applications:

```bash
spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.2 \
streaming_analytics.py
```

---

# Learning Outcomes

This repository demonstrates practical implementation of:

- Apache Spark Fundamentals
- Spark DataFrames
- Spark SQL
- RDD Programming
- Structured Streaming
- Apache Kafka Integration
- Hadoop Ecosystem
- Apache Cassandra Integration
- Performance Optimization
- Big Data Analytics
- Real-Time Data Processing
- Distributed Computing

---
