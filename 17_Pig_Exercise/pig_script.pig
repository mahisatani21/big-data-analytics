-- ============================================
-- Pig Script for Log Analysis
-- Author: Mahi
-- Date: 2026-08-24
-- ============================================

-- Load data from HDFS
logs = LOAD '/pig_input/sample_logs.txt'
USING PigStorage(',')
AS (ip:chararray, endpoint:chararray, status:int, bytes:int);

-- Clean data by removing 404 errors
clean_logs = FILTER logs BY status != 404;

-- Group by IP address
grouped = GROUP clean_logs BY ip;

-- Calculate statistics
ip_stats = FOREACH grouped GENERATE
    group AS ip,
    COUNT(clean_logs) AS request_count,
    SUM(clean_logs.bytes) AS total_bytes;

-- Order results by total bytes in descending order
ordered_stats = ORDER ip_stats BY total_bytes DESC;

-- Store results in HDFS
STORE ordered_stats INTO '/pig_output/ordered_stats'
USING PigStorage('\t');

-- Display top 3 IP addresses
top3 = LIMIT ordered_stats 3;

DUMP top3;
