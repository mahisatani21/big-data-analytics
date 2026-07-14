# Apache Cassandra Exercise – Sparkify Music Streaming

## 📌 Overview

This project demonstrates **Apache Cassandra data modeling** using a music streaming dataset (Sparkify). The exercise focuses on designing query-based tables, inserting data, executing queries, understanding UPSERT operations, and working with Cassandra consistency levels.

---

## 🎯 Objective

- Create a Cassandra keyspace.
- Design query-specific tables.
- Insert sample records.
- Execute CQL queries.
- Demonstrate UPSERT functionality.
- Verify and change consistency levels.

---

## 🛠️ Technologies Used

- Apache Cassandra
- CQL (Cassandra Query Language)
- cqlsh

---

## 📂 Project Structure

```
cassandra-exercise/
│── README.md
│── cassandra_queries.cql
│── screenshots/
│── report.pdf (optional)
```

---

## 🚀 Steps Performed

### 1. Create Keyspace

```sql
CREATE KEYSPACE IF NOT EXISTS sparkify
WITH REPLICATION = {
'class':'SimpleStrategy',
'replication_factor':'1'
};
```

---

### 2. Use Keyspace

```sql
USE sparkify;
```

---

### 3. Create Tables

Three query-specific tables were created:

- `song_info_by_session`
- `song_playing_history_by_user`
- `who_listened_to_song`

---

### 4. Insert Sample Data

Sample records were inserted into all three tables using CQL `INSERT` statements.

---

### 5. Execute Queries

#### Query 1

Retrieve song information by session.

```sql
SELECT * FROM song_info_by_session
WHERE session_id = 100;
```

#### Query 2

Retrieve a user's song playing history.

```sql
SELECT *
FROM song_playing_history_by_user
WHERE user_id = 1
AND session_id = 100;
```

#### Query 3

Find all users who listened to a particular song.

```sql
SELECT *
FROM who_listened_to_song
WHERE song = 'Hey Jude';
```

---

### 6. UPSERT Demonstration

Cassandra automatically updates existing rows when inserting with the same primary key.

```sql
INSERT INTO song_info_by_session
(session_id,item_in_session,artist,song,length)
VALUES
(100,1,'The Beatles','Let It Be',4.03);
```

---

### 7. Consistency Level

Check current consistency level:

```sql
CONSISTENCY;
```

Set consistency level:

```sql
CONSISTENCY ONE;
```

---

## 📊 Features Demonstrated

- Cassandra keyspace creation
- Query-driven data modeling
- Primary key design
- Data insertion
- Query execution
- UPSERT behavior
- Consistency level management

---

## 📸 Output

The project includes screenshots demonstrating:

- Keyspace creation
- Table creation
- Data insertion
- Query execution
- UPSERT operation
- Consistency level verification

---

## 📖 Learning Outcomes

After completing this exercise, you will understand:

- Cassandra's query-first data modeling approach
- Designing tables for specific queries
- Using CQL for CRUD operations
- UPSERT functionality
- Cassandra consistency levels

---

## ✅ Conclusion

This exercise successfully demonstrates the fundamentals of Apache Cassandra by creating a keyspace, designing query-specific tables, inserting and retrieving data, performing UPSERT operations, and verifying consistency levels. It provides practical experience with Cassandra's distributed NoSQL database concepts and query-driven schema design.
