#!/bin/bash

# Get username
USER=$(whoami)

# Clean up existing output directories
echo "Cleaning up existing output directories..."
hdfs dfs -rm -r /user/$USER/analytics/output/daily_aggregates 2>/dev/null
hdfs dfs -rm -r /user/$USER/analytics/output/top_songs 2>/dev/null

# Also clean local output directories
rm -rf ~/hadoop-cassandra-exercise/output/daily_aggregates 2>/dev/null
rm -rf ~/hadoop-cassandra-exercise/output/top_songs 2>/dev/null

# Create fresh output directories in HDFS
hdfs dfs -mkdir -p /user/$USER/analytics/output

# Job 1: Daily Aggregates - Using -file option (compatible with older Hadoop)
echo "Running Daily Aggregation Job..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /user/$USER/analytics/input/batch_plays.csv \
    -output /user/$USER/analytics/output/daily_aggregates \
    -mapper "python3 mapper_daily_aggregate.py" \
    -reducer "python3 reducer_daily_aggregate.py" \
    -file scripts/mapper_daily_aggregate.py \
    -file scripts/reducer_daily_aggregate.py

if [ $? -eq 0 ]; then
    echo "✅ Daily Aggregation Job completed successfully!"
else
    echo "❌ Daily Aggregation Job failed!"
    exit 1
fi

# Job 2: Top 100 Songs
echo "Running Top Songs Job..."
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -input /user/$USER/analytics/input/batch_plays.csv \
    -output /user/$USER/analytics/output/top_songs \
    -mapper "python3 mapper_top_songs.py" \
    -reducer "python3 reducer_top_songs.py" \
    -file scripts/mapper_top_songs.py \
    -file scripts/reducer_top_songs.py

if [ $? -eq 0 ]; then
    echo "✅ Top Songs Job completed successfully!"
else
    echo "❌ Top Songs Job failed!"
    exit 1
fi

# Check output files
echo "Checking output files..."
hdfs dfs -ls /user/$USER/analytics/output/daily_aggregates/
hdfs dfs -ls /user/$USER/analytics/output/top_songs/

# Download results
echo "Downloading results from HDFS..."
mkdir -p ~/hadoop-cassandra-exercise/output/daily_aggregates
mkdir -p ~/hadoop-cassandra-exercise/output/top_songs

hdfs dfs -get /user/$USER/analytics/output/daily_aggregates/part-00000 ~/hadoop-cassandra-exercise/output/daily_aggregates/ 2>/dev/null
if [ -f ~/hadoop-cassandra-exercise/output/daily_aggregates/part-00000 ]; then
    echo "✅ Downloaded daily aggregates"
    echo "Sample output:"
    head -5 ~/hadoop-cassandra-exercise/output/daily_aggregates/part-00000
else
    echo "⚠️ No daily aggregates output file found"
fi

hdfs dfs -get /user/$USER/analytics/output/top_songs/part-00000 ~/hadoop-cassandra-exercise/output/top_songs/ 2>/dev/null
if [ -f ~/hadoop-cassandra-exercise/output/top_songs/part-00000 ]; then
    echo "✅ Downloaded top songs"
    echo "Sample output:"
    head -5 ~/hadoop-cassandra-exercise/output/top_songs/part-00000
else
    echo "⚠️ No top songs output file found"
fi

echo "✅ Hadoop jobs completed successfully!"
