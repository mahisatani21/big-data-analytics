# Apache Pig Hands-On — Web Log Analysis

## 📌 Overview

This project demonstrates **Apache Pig** for processing and analyzing web server log data using both **Local Mode** and **Hadoop MapReduce Mode**.

The exercise covers basic Pig operations such as `LOAD`, `FILTER`, `GROUP`, and `FOREACH`, as well as advanced operations including `JOIN`, built-in functions, HDFS storage, and batch execution using a Pig script.

---

## 🎯 Objective

The main objectives of this exercise are:

- Process web log data using Apache Pig.
- Execute Pig programs in Local Mode.
- Execute Pig programs using Hadoop MapReduce.
- Load data from the local filesystem and HDFS.
- Filter HTTP error requests.
- Group requests by IP address.
- Calculate request counts and total bytes.
- Perform JOIN operations between log and user datasets.
- Use Pig built-in functions such as `MATCHES` and `UPPER`.
- Store processed results in HDFS.
- Execute Pig programs using a batch `.pig` script.

---

## 🛠️ Technologies Used

| Technology | Version |
|---|---|
| Apache Pig | 0.17.0 |
| Apache Hadoop | 3.4.2 |
| Java | OpenJDK 8 |
| Operating System | Ubuntu / WSL2 |
| HDFS | Hadoop Distributed File System |
| Execution | Local Mode & MapReduce Mode |

---

## 📂 Project Structure

```text
pig-hands-on/
│
├── sample_logs.txt
├── user_data.txt
├── pig_script.pig
├── README.md
└── screenshots/
    ├── 01_local_mode.png
    ├── 02_data_processing.png
    ├── 03_hadoop_services.png
    ├── 04_hdfs_input.png
    ├── 05_join_operation.png
    ├── 06_builtin_functions.png
    ├── 07_batch_script.png
    └── 08_hdfs_output.png
