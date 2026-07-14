from cassandra.cluster import Cluster

cluster = Cluster(["localhost"])
session = cluster.connect("streaming_analytics")

print("Loading Daily Aggregates...")

with open("/home/mahi/hadoop-cassandra-exercise/output/daily_aggregates.txt") as f:

    for line in f:

        line=line.strip()

        if not line:
            continue

        date,total_plays,unique_users,avg_duration,top_song,top_artist=line.split("\t")

        session.execute("""
        INSERT INTO daily_aggregates
        (date,total_plays,unique_users,avg_duration,top_song,top_artist)
        VALUES (%s,%s,%s,%s,%s,%s)
        """,(date,
             int(total_plays),
             int(unique_users),
             float(avg_duration),
             top_song,
             top_artist))

print("Loading Top Songs...")

with open("/home/mahi/hadoop-cassandra-exercise/output/top_songs.txt") as f:

    for line in f:

        line=line.strip()

        if not line:
            continue

        date,rank,song,artist,count=line.split("\t")

        session.execute("""
        INSERT INTO top_songs_daily
        (date,rank,song,artist,play_count)
        VALUES (%s,%s,%s,%s,%s)
        """,(date,
             int(rank),
             song,
             artist,
             int(count)))

cluster.shutdown()

print("Results Loaded Successfully")
