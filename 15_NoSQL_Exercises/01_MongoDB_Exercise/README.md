# MongoDB Exercise 1: E-Commerce Product Catalog

## Overview

This project demonstrates the implementation of an **E-Commerce Product Catalog system using MongoDB**. The exercise focuses on MongoDB document-based database operations, schema flexibility, CRUD operations, querying techniques, aggregation, and indexing.

The product catalog stores information about different types of products such as electronics, books, footwear, and gaming products. MongoDB's flexible schema design allows storing different attributes for different product categories within the same collection.

---

# Objectives

The main objectives of this exercise are:

- Understand MongoDB database and collection creation.
- Perform CRUD operations on MongoDB documents.
- Insert and manage product information.
- Execute different types of MongoDB queries.
- Work with nested documents and arrays.
- Demonstrate MongoDB schema flexibility.
- Perform aggregation operations.
- Create and analyze indexes for improving query performance.

---

# Technologies Used

- MongoDB
- MongoDB Shell (mongosh)
- NoSQL Database Concepts
- JSON/BSON Document Structure

---

# Database Structure

## Database Name

```
ecommerce_db
```

## Collection Name

```
products
```

---

# Product Document Features

Each product document contains information such as:

- Product SKU
- Product name
- Category
- Price
- Stock availability
- Product specifications
- Tags
- Release date
- Ratings
- Customer reviews

Example product categories:

- Electronics
- Books
- Footwear
- Gaming

---

# Implementation Steps

## Step 1: Database Setup

- Connected to MongoDB using MongoDB Shell.
- Created and selected the `ecommerce_db` database.
- Verified successful database connection.

---

## Step 2: Insert Documents

Product documents were inserted into the MongoDB collection.

Operations performed:

- Inserted a single product document.
- Inserted multiple product documents.
- Stored nested objects such as specifications.
- Stored arrays such as tags and reviews.

---

## Step 3: Basic Queries

Different queries were executed to retrieve product information.

Operations performed:

- Display all products.
- Search products by category.
- Find products based on price conditions.
- Retrieve products using rating filters.
- Search nested document fields.
- Search products using tags.
- Sort products based on price.
- Limit query results.
- Display selected fields using projection.

---

## Step 4: Update Operations

Product information was modified using MongoDB update operations.

Operations performed:

- Increased product stock quantity.
- Added new product specifications.
- Added new product tags.
- Added customer reviews.
- Updated multiple products.
- Renamed fields.
- Removed fields.

---

## Step 5: Delete Operations

Deletion operations were performed to manage product data.

Operations performed:

- Deleted a specific product.
- Deleted products based on stock conditions.
- Verified remaining documents.
- Counted available products.

---

## Step 6: Schema Flexibility Demonstration

MongoDB schema flexibility was demonstrated by inserting a product with a completely different structure.

A gaming product was added with different attributes:

- CPU information
- GPU information
- Storage details
- Included accessories
- Region availability
- Digital availability

This shows that MongoDB allows different document structures within the same collection.

---

## Step 7: Index Creation

Indexes were created to improve query performance.

Indexes implemented:

- Single field index
- Unique index
- Compound index
- Text search index

Query execution plans were analyzed to understand how MongoDB uses indexes for optimization.

---

# MongoDB Concepts Covered

## CRUD Operations

### Create
Adding new product documents into the collection.

### Read
Retrieving product information using different queries.

### Update
Modifying existing product documents.

### Delete
Removing unwanted product documents.

---

# Schema Flexibility

MongoDB does not require a fixed schema like relational databases.

Advantages:

- Easy to add new fields.
- Supports different document structures.
- Suitable for rapidly changing applications.
- Handles semi-structured data efficiently.

Limitations:

- Data validation becomes more complex.
- Maintaining consistency requires careful design.
- Queries may become complicated with highly different document structures.

---

# Indexing

Indexes improve database performance by allowing MongoDB to search documents efficiently without scanning the entire collection.

Benefits:

- Faster query execution.
- Improved search performance.
- Efficient sorting and filtering.

Types of indexes used:

- Single field index
- Unique index
- Compound index
- Text index

---

# Key Learnings

Through this exercise, the following concepts were learned:

- MongoDB document-based storage.
- Working with JSON-like BSON documents.
- CRUD operations in MongoDB.
- Querying nested documents and arrays.
- Aggregation framework.
- Schema flexibility.
- Database indexing and optimization.

---

# Conclusion

The MongoDB E-Commerce Product Catalog exercise successfully demonstrated how MongoDB can be used to build flexible and scalable applications.

The implementation covered database creation, document management, CRUD operations, advanced querying, schema flexibility, aggregation, and indexing.

MongoDB's document-oriented approach makes it suitable for modern applications where data structures frequently change and different types of information need to be stored efficiently.
