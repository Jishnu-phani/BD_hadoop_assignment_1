#!/usr/bin/env python3
import sys
for line in sys.stdin:
    d = line.strip().split()
    if len(d) > 2:
        # broken = 0.0 if len(data) == 4 else float(data[4])
        if len(d) == 4:
            broken = 0.0
        else:
            broken = float(d[4])
        req_id, client_id, endpoint, timestamp = d[0], d[1], d[2], d[3]
        stat = 500 if broken == 3 else 0
        print(f"{timestamp} {req_id} {client_id} {endpoint} {broken} {stat}")
    elif len(d) == 2:
        req_id, pred_stat = d
        print(f"{req_id} {pred_stat}")
