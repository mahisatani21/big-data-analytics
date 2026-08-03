# Neo4j Installation and Hands-On Exercise

## Overview

This document explains the installation of Neo4j in WSL Ubuntu and performing graph database operations using Neo4j Browser and Cypher Query Language.

---

# Part 1: Neo4j Installation in WSL

## Step 1: Install Java

Neo4j requires Java Runtime Environment. OpenJDK 17 was installed as the required dependency.

## Step 2: Verify Java Installation

The Java installation was verified to ensure compatibility with Neo4j.

## Step 3: Add Neo4j Repository

The official Neo4j repository was added by importing the Neo4j public key and configuring the package source.

## Step 4: Install Neo4j

Neo4j Community Edition was installed using the Ubuntu package manager.

## Step 5: Start Neo4j Service

The Neo4j database service was started and checked to confirm that it was running successfully.

## Step 6: Access Neo4j Browser

Neo4j Browser was accessed through:

**http://localhost:7474**

Default login:

- Username: neo4j
- Password: password123

---

# Part 2: Neo4j Database Design

## Graph Model

The e-learning system was modeled as a graph database.

The graph contains:

### Nodes

#### Student Nodes

Stores:

- Student ID
- Student Name
- Email Address

#### Course Nodes

Stores:

- Course ID
- Course Title
- Instructor Name

---

## Relationships

The following relationships were created:

### ENROLLED_IN

Represents student course enrollment.

Relationship properties:

- Progress percentage
- Course completion status

### FOLLOWS

Represents student social connections.

---

# Part 3: Neo4j Hands-On Exercise

## Node Creation

Created multiple student nodes representing learners in the e-learning platform.

Created course nodes representing available courses.

---

## Relationship Creation

Created enrollment relationships between students and courses.

Created follow relationships between students to represent social connections.

---

# Query Operations Performed

The following graph queries were executed:

## Student and Course Retrieval

- Retrieve all students
- Retrieve all courses
- Display complete graph information

## Enrollment Analysis

- Find courses enrolled by a specific student
- Find students enrolled in a particular course
- Display course progress and completion status

## Social Network Analysis

- Find students following a specific student
- Find students followed by a specific student
- Identify mutual followers

---

# Advanced Graph Queries

Performed advanced graph analysis including:

- Course recommendation based on student connections
- Finding shortest paths between students
- Identifying students with completed courses
- Counting followers for each student
- Calculating course enrollment statistics

---

# Update Operations

Performed graph updates including:

- Updating course progress
- Changing course completion status
- Adding new students
- Creating new enrollment relationships
- Adding new follow relationships

---

# Delete Operations

Performed deletion operations including:

- Removing specific students
- Removing relationships
- Clearing graph data when required

---

# Graph Visualization

The Neo4j Browser visualization feature was used to:

- Display the complete graph structure
- Explore student connections
- Analyze relationships between students and courses

---

# Technologies Used

- Neo4j Community Edition
- Neo4j Browser
- Cypher Query Language
- Ubuntu WSL
- Graph Database Concepts

---

# Learning Outcomes

After completing this exercise, the following concepts were covered:

- Neo4j installation and configuration
- Graph database modeling
- Nodes and relationships
- Cypher query language
- Graph traversal
- Relationship analysis
- Graph-based recommendations
- Data visualization

---

# Conclusion

Neo4j was successfully installed in WSL and an e-learning graph database was created. The exercise demonstrated how graph databases represent connected data and how Cypher queries can be used for relationship-based analysis.
