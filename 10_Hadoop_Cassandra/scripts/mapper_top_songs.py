#!/usr/bin/env python3

import sys
from datetime import datetime

for line in sys.stdin:

    line=line.strip()

    if not line or line.startswith("user_id"):
        continue

    parts=line.split(",")

    if len(parts)<6:
        continue

    try:

        timestamp=datetime.strptime(parts[1],"%Y-%m-%d %H:%M:%S")

        song=parts[2]

        artist=parts[3]

        date=timestamp.strftime("%Y-%m-%d")

        print(f"{date}_{song}\t{artist},1")

    except:
        continue
