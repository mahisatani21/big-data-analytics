# Apache Hive Hands-On Exercise — Sales Data Analysis

## 📌 Project Overview

This project demonstrates the use of **Apache Hive with Hadoop** for storing, querying, analyzing, and optimizing structured sales data.

The exercise covers basic Hive table operations, SQL-based data analysis, JOIN operations, external tables, partitioning, partition pruning, query execution plans, and table metadata.

---

## 🎯 Objectives

The main objectives of this exercise are to:

- Create and manage a Hive database.
- Create a managed Hive table.
- Load CSV data into Hive.
- Perform filtering and sorting operations.
- Perform aggregation using `SUM()`, `AVG()`, and `COUNT()`.
- Use `GROUP BY` and `HAVING`.
- Perform JOIN operations between Hive tables.
- Create an external table.
- Demonstrate table partitioning.
- Query partitioned data using partition filters.
- Understand partition pruning.
- Generate query execution plans using `EXPLAIN`.
- Explore Hive table metadata using `DESCRIBE` and `DESCRIBE FORMATTED`.
- Demonstrate Hive optimization concepts.

---

## 🛠️ Technologies Used

| Technology | Version / Description |
|---|---|
| Hadoop | 3.4.2 |
| Apache Hive | 3.1.3 |
| Java | OpenJDK 8 |
| HDFS | Hadoop Distributed File System |
| YARN | Hadoop Resource Management |
| SQL | HiveQL |
| Operating System | Linux / WSL |

---

## 📂 Project Structure

```text
hive-hands-on/
│
├── README.md
│
├── sales_data.csv
│
└── customers.csv
