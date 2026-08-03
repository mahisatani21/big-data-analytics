# MongoDB Installation and Hands-On Exercise

## Overview

This document explains the installation of MongoDB in WSL Ubuntu and performing basic MongoDB database operations using MongoDB Shell.

---

# Part 1: MongoDB Installation in WSL

## Step 1: Update Ubuntu Packages

Update and upgrade Ubuntu packages before installing MongoDB.

## Step 2: Install Required Dependencies

Install required tools such as curl, wget, gnupg, and lsb-release.

## Step 3: Add MongoDB Repository

Import the MongoDB public key and configure the official MongoDB repository.

## Step 4: Install MongoDB

Install MongoDB Community Edition using the Ubuntu package manager.

## Step 5: Start MongoDB Service

Start the MongoDB service and verify that it is running successfully.

## Step 6: Verify MongoDB Connection

Connect to MongoDB using MongoDB Shell (`mongosh`) and confirm that the database server is working.

---

# Part 2: MongoDB Database Setup

## Database Creation

Created an e-learning database named:

**elearning_db**

A collection named:

**students**

was created to store student information.

---

# Part 3: MongoDB Hands-On Exercise

## Data Model

The student collection contains:

- Student ID
- Student Name
- Email Address
- Enrolled Courses
- Course Progress
- Course Status
- Student Follow Relationships

---

## CRUD Operations Performed

### Create Operations

Performed document insertion for multiple students with course enrollment details.

### Read Operations

Executed queries to:

- View all students
- Find students enrolled in specific courses
- Find students based on course progress
- Identify students following multiple users
- Search students without courses

### Update Operations

Performed updates such as:

- Modifying course progress
- Adding new courses to students
- Updating course completion status
- Modifying embedded course information

### Delete Operations

Performed deletion operations including:

- Removing student records
- Removing specific courses from student documents

---

# Aggregation Operations

Implemented MongoDB aggregation pipelines for:

- Counting students per course
- Calculating average course progress
- Finding most followed students

---

# Indexing and Performance Optimization

Created indexes on student identifiers to improve query performance.

Analyzed query execution statistics using MongoDB explain functionality.

---

# Technologies Used

- MongoDB Community Edition
- MongoDB Shell (mongosh)
- Ubuntu WSL
- NoSQL Database Concepts

---

# Learning Outcomes

After completing this exercise, the following concepts were covered:

- MongoDB installation and configuration
- Database and collection creation
- Document-based data storage
- CRUD operations
- Embedded documents and arrays
- Aggregation framework
- Indexing and query optimization

---

# Conclusion

MongoDB was successfully installed in WSL and an e-learning database was implemented. The exercise demonstrated practical usage of MongoDB for storing and analyzing semi-structured data.
