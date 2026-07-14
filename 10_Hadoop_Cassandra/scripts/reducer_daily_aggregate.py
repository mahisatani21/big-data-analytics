#!/usr/bin/env python3

import sys
from collections import defaultdict

current_date=None

users=set()

songs_count=defaultdict(int)

artists_count=defaultdict(int)

total_duration=0

total_plays=0

for line in sys.stdin:

    line=line.strip()

    if not line:
        continue

    date,data=line.split("\t",1)

    user_id,song,artist,duration=data.split(",")

    duration=float(duration)

    if current_date is None:
        current_date=date

    if date!=current_date:

        top_song=max(songs_count.items(),key=lambda x:x[1])[0]

        top_artist=max(artists_count.items(),key=lambda x:x[1])[0]

        print(
            f"{current_date}\t{total_plays}\t{len(users)}\t{total_duration/len(users):.2f}\t{top_song}\t{top_artist}"
        )

        current_date=date

        users=set()

        songs_count=defaultdict(int)

        artists_count=defaultdict(int)

        total_duration=0

        total_plays=0

    users.add(user_id)

    songs_count[song]+=1

    artists_count[artist]+=1

    total_duration+=duration

    total_plays+=1

if current_date:

    top_song=max(songs_count.items(),key=lambda x:x[1])[0]

    top_artist=max(artists_count.items(),key=lambda x:x[1])[0]

    print(
        f"{current_date}\t{total_plays}\t{len(users)}\t{total_duration/len(users):.2f}\t{top_song}\t{top_artist}"
    )
