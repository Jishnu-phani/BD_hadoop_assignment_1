#!/usr/bin/env python3
import sys
for line in sys.stdin:
    d = line.strip().split(" ")
    if len(d) == 4:
        req_id, client_id, endpoint, stat = d
        print(f"{client_id} {endpoint} {stat} {pred}")
    elif len(d) == 2:
        req_id, pred = d