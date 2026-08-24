# Big Data Analytics — Apache Pig Micro Project

<p align="center">
  <b>Big Data Analytics Micro Project</b><br>
  Hadoop HDFS • Apache Pig • MapReduce • Data Processing
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Domain-Big%20Data%20Analytics-blue" alt="Big Data Analytics">
  <img src="https://img.shields.io/badge/Hadoop-3.4.2-yellow" alt="Hadoop">
  <img src="https://img.shields.io/badge/Apache%20Pig-0.17.0-orange" alt="Apache Pig">
  <img src="https://img.shields.io/badge/Execution-Local%20%26%20MapReduce-green" alt="Execution">
  <img src="https://img.shields.io/badge/Platform-Linux%20%2F%20WSL2-lightgrey" alt="Platform">
  <img src="https://img.shields.io/badge/Status-Completed-success" alt="Status">
</p>

---

## 📌 Project Overview

This project demonstrates practical **Big Data processing and analytics using Apache Pig and the Hadoop ecosystem**.

The project focuses on processing web server log data using **Pig Latin**, with execution demonstrated in both **Local Mode** and **Hadoop MapReduce Mode**.

The project covers the complete workflow from local data creation and loading to distributed processing, filtering, grouping, aggregation, joining datasets, applying built-in functions, storing results in HDFS, and executing Pig programs in batch mode.

The implementation was carried out in a **Linux/WSL2 environment** using Hadoop 3.4.2 and Apache Pig 0.17.0.

---

## 🎯 Objectives

The main objectives of this project are:

- Understand the fundamentals of Apache Pig.
- Configure and execute Pig in Local Mode.
- Process structured log data using Pig Latin.
- Load data from the local filesystem.
- Load data from HDFS.
- Perform filtering and grouping operations.
- Calculate request counts and total bytes.
- Sort analytical results.
- Perform JOIN operations between datasets.
- Use Pig built-in string and filtering functions.
- Store processed results in HDFS.
- Execute Pig programs using batch scripts.
- Understand the relationship between Pig and Hadoop MapReduce.

---

## 🛠️ Technology Stack

| Technology | Version / Purpose |
|---|---|
| Hadoop | 3.4.2 |
| Apache Pig | 0.17.0 |
| HDFS | Distributed File Storage |
| YARN | Resource Management |
| MapReduce | Distributed Processing |
| Java | OpenJDK |
| Linux / WSL2 | Execution Environment |
| Git | Version Control |
| GitHub | Project Repository |

---

## 📂 Project Structure

```text
Micro_Project/
│
├── charts/
│   └── Generated charts and visualizations
│
├── data/
│   └── Input datasets used in the project
│
├── output/
│   └── Generated analytical outputs
│
├── screenshots/
│   └── Execution and result screenshots
│
├── scripts/
│   └── Pig scripts and related source files
│
├── Micro Project Report.docx
│   └── Detailed project report
│
├── Micro Project Report.pdf
│   └── PDF version of the project report
│
└── README.md
    └── Project documentation
```

## 🏗️ Project Architecture

The project follows a Big Data processing architecture using **Hadoop HDFS, Apache Pig, Apache Spark, and Hive** for distributed data storage, processing, and analysis.

```text
                         ┌─────────────────────────┐
                         │      Input Dataset      │
                         │                         │
                         │  CSV / Text / Log Data  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │      Data Ingestion     │
                         │                         │
                         │     Hadoop HDFS         │
                         └────────────┬────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
                    ▼                 ▼                 ▼
          ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
          │  Apache Pig    │ │ Apache Hive    │ │ Apache Spark   │
          │                │ │                │ │                │
          │ ETL & Log      │ │ SQL-based      │ │ Distributed    │
          │ Processing     │ │ Analysis       │ │ Processing     │
          └───────┬────────┘ └───────┬────────┘ └───────┬────────┘
                  │                  │                  │
                  └──────────────────┼──────────────────┘
                                     │
                                     ▼
                         ┌─────────────────────────┐
                         │    Data Processing &    │
                         │       Analytics         │
                         │                         │
                         │ • Filtering             │
                         │ • Grouping              │
                         │ • Aggregation           │
                         │ • Join Operations      │
                         │ • Statistical Analysis  │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │       Output Layer      │
                         │                         │
                         │ • Processed Data        │
                         │ • Analysis Results      │
                         │ • Reports               │
                         │ • Charts / Visuals      │
                         └────────────┬────────────┘
                                      │
                                      ▼
                         ┌─────────────────────────┐
                         │     Documentation       │
                         │                         │
                         │ README │ Report │       │
                         │ Screenshots │ Results   │
                         └─────────────────────────┘
