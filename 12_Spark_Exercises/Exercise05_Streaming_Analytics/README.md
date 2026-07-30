# Exercise 5 - Streaming Analytics

This project demonstrates real-time data processing using Apache Spark Structured Streaming with Kafka. It performs window-based aggregations, watermarking, and live analytics on streaming data.

## Technologies Used

- Apache Spark 4.1.2
- PySpark
- Apache Kafka (KRaft Mode)
- Python 3
- Java (JDK)
- WSL (Ubuntu)
- Spark Structured Streaming

## Files

- streaming_analytics.py

## Run

```bash
spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.13:4.1.2 \
streaming_analytics.py
```
