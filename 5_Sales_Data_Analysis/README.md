# Sales Data Analysis using Hadoop

This repository demonstrates **Sales Data Analysis using Hadoop** with custom **Python Mapper and Reducer** scripts. The project showcases how Hadoop MapReduce can be used to process a large sales dataset for city-wise sales analysis, monthly sales trends, product quantity analysis, and data visualization.

## Objective

The objective of this project is to:

* Generate a large sales dataset.
* Process the dataset using Hadoop Streaming.
* Implement custom Python Mapper and Reducer programs.
* Perform city-wise sales analysis.
* Analyze monthly sales trends.
* Identify top-selling products.
* Visualize the analysis results using Python.

## Prerequisites

* Ubuntu Linux
* Apache Hadoop installed and configured
* Java (OpenJDK 11 or later)
* Python 3
* Hadoop Streaming JAR
* Pandas
* Matplotlib

## Workflow

The project follows these steps:

1. Generate a sales dataset containing 50,000 records.
2. Verify the generated dataset.
3. Develop a Python Mapper for city-wise sales.
4. Develop a Python Reducer for aggregating city sales.
5. Test the Mapper and Reducer locally.
6. Upload the dataset to HDFS.
7. Execute the Hadoop Streaming job.
8. Analyze the city-wise sales results.
9. Perform monthly sales analysis.
10. Analyze product quantities.
11. Visualize the results using Python and Matplotlib.

## Features

* Large-scale sales dataset generation
* Hadoop Streaming with Python
* Custom Mapper implementation
* Custom Reducer implementation
* City-wise sales analysis
* Monthly sales trend analysis
* Product quantity analysis
* Top-performing city identification
* Data visualization using bar charts

## Repository Contents

* Sales dataset generator
* Python Mapper scripts
* Python Reducer scripts
* Hadoop Streaming execution steps
* Sales analysis results
* Visualization program
* Execution screenshots

## Analysis Performed

The project includes the following analyses:

* City-wise total sales
* Transaction count by city
* Average transaction value
* Monthly sales trends
* Product quantity analysis
* Top-selling cities
* Top-selling products

## Expected Output

The Hadoop Streaming job processes the sales dataset using custom Python Mapper and Reducer scripts. The generated output includes city-wise sales summaries, transaction counts, monthly sales trends, and product quantity statistics. The final results are visualized using Python and Matplotlib.

## Learning Outcomes

After completing this project, you will be able to:

* Understand Hadoop Streaming architecture.
* Develop custom Python Mapper and Reducer programs.
* Process large datasets using Hadoop MapReduce.
* Perform distributed sales data analysis.
* Analyze city-wise and monthly sales trends.
* Generate visualizations from Hadoop output using Python.
* Apply Hadoop Streaming for real-world data analytics.

## Project Structure

* Objective
* Procedure
* Dataset Generation
* Mapper Implementation
* Reducer Implementation
* Local Testing
* Hadoop Streaming Execution
* Sales Analysis
* Visualization
* Screenshots
* Conclusion

## Conclusion

This project demonstrates the successful implementation of Hadoop Streaming using custom Python Mapper and Reducer scripts for large-scale sales data analysis. By processing a dataset containing 50,000 sales records, the project performs city-wise sales aggregation, monthly sales trend analysis, product quantity analysis, and visualization of results. It provides practical experience in distributed data processing and analytics using Hadoop and Python.

## License

This repository is intended for educational and learning purposes.
