#!/usr/bin/env python3
import sys
for line in sys.stdin:
    d = line.strip().split(" ")
    if len(d) == 4:
        req_id, c_id, endpoint, stat = d
        print(f"{req_id} {c_id} {endpoint} {stat}")
    elif len(d) == 2:
        req_id, pred_status = d
        # print(f"{x},{y}")
        print(f"{req_id} {pred_status}")
