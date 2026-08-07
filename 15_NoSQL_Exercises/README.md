# NoSQL Database Exercises

## Overview

This repository contains implementations of NoSQL database exercises using **MongoDB** and **Neo4j**. The exercises demonstrate document-based storage, graph modeling, data querying, aggregation, relationship analysis, and database comparison.

---

# Tasks Summary

## Task 1: MongoDB - E-Commerce Product Catalog

Implemented an e-commerce product catalog using MongoDB.

### Key Concepts Covered:
- Creating and inserting documents.
- Performing CRUD operations.
- Querying documents using filters.
- Updating and deleting records.
- Demonstrating schema flexibility.
- Creating indexes for faster searching.

### Features Implemented:
- Product storage with different categories.
- Product search based on price, rating, and specifications.
- Inventory updates.
- Text search indexing.

---

## Task 2: MongoDB - Aggregation Pipeline

Implemented sales analytics using MongoDB aggregation framework.

### Key Concepts Covered:
- Aggregation pipeline stages.
- `$match`, `$group`, `$unwind`, `$project`.
- Revenue analysis.
- Customer spending analysis.
- Product performance analysis.

### Features Implemented:
- Revenue by category.
- Average order value calculation.
- Customer lifetime value.
- Top-selling products.
- Daily revenue tracking.

---

## Task 3: Neo4j - Social Network Analysis

Implemented a social network model using Neo4j graph database.

### Key Concepts Covered:
- Creating nodes and relationships.
- Cypher query language.
- Graph traversal.
- Shortest path analysis.
- Recommendation systems.

### Features Implemented:
- User node creation.
- FOLLOWS relationship modeling.
- Finding followers and mutual connections.
- Friend recommendations.
- Influence and network analysis.

---

## Task 4: MongoDB vs Neo4j Comparison

Compared MongoDB and Neo4j by implementing the same social network functionality.

### Key Concepts Covered:
- Document-based modeling vs graph-based modeling.
- Relationship handling.
- Query complexity comparison.
- Database suitability analysis.

### Comparison Summary:

| Feature | MongoDB | Neo4j |
|---------|---------|-------|
| Data Model | Documents | Graph |
| Relationships | References/Arrays | Nodes and Edges |
| Query Style | Aggregation | Cypher Traversal |
| Best For | Flexible Data | Connected Data |
| Use Cases | Catalogs, Analytics | Social Networks, Recommendations |

---

# Technologies Used

- MongoDB
- MongoDB Shell (mongosh)
- Neo4j
- Cypher Query Language

---

# Conclusion

These exercises demonstrate the strengths of NoSQL databases. MongoDB provides flexible document storage and powerful aggregation capabilities, while Neo4j provides efficient relationship-based analysis through graph modeling. Both databases are suitable for different application requirements.

