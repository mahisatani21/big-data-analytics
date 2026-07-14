# Hadoop Installation Guide (Single Node Setup)

This repository provides a step-by-step guide to install and configure Apache Hadoop in **Single Node (Standalone) mode** on **Ubuntu Linux**. It covers Java installation, SSH configuration, Hadoop setup, environment configuration, HDFS initialization, and verification of the installation.

## Prerequisites

* Ubuntu Linux
* Sudo privileges
* Internet connection
* OpenJDK 11
* OpenSSH Server and Client

## Software Used

* Apache Hadoop 3.4.1
* OpenJDK 11
* Ubuntu Linux

## Installation Steps

1. Update the Ubuntu system.
2. Install Java (OpenJDK 11).
3. Create a dedicated Hadoop user.
4. Configure passwordless SSH.
5. Download and extract Apache Hadoop.
6. Configure Hadoop environment variables.
7. Configure Hadoop configuration files:

   * hadoop-env.sh
   * core-site.xml
   * hdfs-site.xml
   * mapred-site.xml
   * yarn-site.xml
8. Create HDFS NameNode and DataNode directories.
9. Format the Hadoop NameNode.
10. Start HDFS and YARN services.
11. Verify running Hadoop services.
12. Access Hadoop web interfaces.
13. Stop Hadoop services when finished.

## Configuration Files

The installation includes configuration of the following Hadoop files:

* hadoop-env.sh
* core-site.xml
* hdfs-site.xml
* mapred-site.xml
* yarn-site.xml

## Verification

After installation, verify Hadoop using:

* Java version
* Hadoop version
* Running Java processes (JPS)
* HDFS report
* HDFS directory listing

## Hadoop Web Interfaces

* **NameNode UI:** [http://localhost:9870](http://localhost:9870)
* **ResourceManager UI:** [http://localhost:8088](http://localhost:8088)

## Repository Contents

* Hadoop Installation Guide
* Configuration steps
* Verification commands
* Hadoop startup and shutdown procedures

## Learning Outcomes

After completing this guide, you will be able to:

* Install Apache Hadoop on Ubuntu.
* Configure a Single Node Hadoop cluster.
* Set up HDFS and YARN.
* Start and stop Hadoop services.
* Verify successful Hadoop installation.
* Access Hadoop management web interfaces.

## Notes

* This guide is intended for educational purposes and local development.
* Ensure all commands are executed in the order provided.
* Administrative (sudo) privileges are required during installation.

## License

This project is intended for learning and educational use.
