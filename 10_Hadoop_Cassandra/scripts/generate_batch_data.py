
import random
import csv
from datetime import datetime, timedelta
from pathlib import Path

artists = [
    'The Beatles','Led Zeppelin','Pink Floyd','Queen','Nirvana',
    'Michael Jackson','Madonna','U2','Eagles','AC/DC'
]

songs = [
    'Hey Jude','Stairway to Heaven','Comfortably Numb',
    'Bohemian Rhapsody','Smells Like Teen Spirit',
    'Billie Jean','Like a Prayer','With or Without You',
    'Hotel California','Back in Black'
]

output_dir = Path.home() / "hadoop-cassandra-exercise" / "data"
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "batch_plays.csv"

with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)

    writer.writerow([
        "user_id",
        "timestamp",
        "song",
        "artist",
        "session_id",
        "duration"
    ])

    start_date = datetime(2024,1,1)

    for i in range(100000):

        user_id = random.randint(1,1000)

        date = start_date + timedelta(days=random.randint(0,730))

        timestamp = date + timedelta(
            hours=random.randint(0,23),
            minutes=random.randint(0,59)
        )

        song = random.choice(songs)
        artist = random.choice(artists)

        session_id = random.randint(1000,9999)

        duration = round(random.uniform(2.5,10.0),2)

        writer.writerow([
            user_id,
            timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            song,
            artist,
            session_id,
            duration
        ])

print(f"File Created : {output_file}")
print("Records : 100000")
