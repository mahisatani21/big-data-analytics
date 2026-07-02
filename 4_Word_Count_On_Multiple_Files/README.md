# Hadoop MapReduce Word Count on Multiple Files

This repository demonstrates how to execute the **Hadoop MapReduce Word Count** application on multiple input files stored in the **Hadoop Distributed File System (HDFS)**. The project covers creating an HDFS directory, uploading multiple text files, running the Word Count program, and identifying the most frequently occurring words from the generated output.

## Objective

The objective of this project is to:

* Create an HDFS directory.
* Create multiple input text files.
* Upload the files to HDFS.
* Execute the Hadoop MapReduce Word Count program on all files collectively.
* View the generated output.
* Identify the top three most frequent words from the output.

## Prerequisites

* Ubuntu Linux
* Apache Hadoop installed and configured
* Java (OpenJDK 11 or later)
* HDFS and YARN services running
* Hadoop MapReduce Examples JAR

## Workflow

The project follows these steps:

1. Create a directory in HDFS.
2. Create multiple input text files.
3. Upload the files to HDFS.
4. Verify the uploaded files.
5. Execute the Hadoop MapReduce Word Count program.
6. View the generated output.
7. Identify the top three most frequent words.

## Repository Contents

* HDFS directory creation
* Multiple input file creation
* File upload to HDFS
* File verification
* Hadoop MapReduce execution
* Word count output
* Top three frequent words analysis
* Execution screenshots

## Expected Output

The Hadoop MapReduce application processes all input files together and generates an output containing the frequency of every word. The results are stored in the HDFS output directory, and Linux commands are used to display the three most frequently occurring words.

## Learning Outcomes

After completing this project, you will be able to:

* Create and manage directories in HDFS.
* Upload multiple files to HDFS.
* Execute Hadoop MapReduce applications on multiple input files.
* Analyze the generated Word Count results.
* Identify the most frequent words using Linux commands.
* Understand distributed processing of multiple datasets using Hadoop.

## Project Structure

* Objective
* Procedure
* Source Code
* Execution Screenshots
* Result Analysis
* Conclusion

## Conclusion

This project demonstrates the successful execution of the Hadoop MapReduce Word Count application on multiple input files stored in HDFS. The experiment illustrates how Hadoop efficiently processes distributed data across multiple files, generates word frequency statistics, and enables further analysis such as identifying the most frequently occurring words.

## License

This repository is intended for educational and learning purposes.

