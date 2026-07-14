#!/usr/bin/env python3

import sys
from collections import defaultdict

current_date = None
song_counts = defaultdict(int)
song_artists = {}

def emit_results(date):
    rank = 1
    for (song, artist), count in sorted(song_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"{date}\t{rank}\t{song}\t{artist}\t{count}")
        rank += 1

for line in sys.stdin:
    line = line.strip()

    if not line:
        continue

    key, value = line.split("\t")

    date, song = key.split("_", 1)
    artist, count = value.split(",")

    count = int(count)

    if current_date is None:
        current_date = date

    if date != current_date:
        emit_results(current_date)
        song_counts = defaultdict(int)
        song_artists = {}
        current_date = date

    song_counts[(song, artist)] += count

if current_date is not None:
    emit_results(current_date)