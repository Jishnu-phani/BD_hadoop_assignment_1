#!/usr/bin/env python3
import sys
current_client = ""
for line in sys.stdin:
    d = line.strip().split(" ")    
    cli_id, endpoint, stat, pred_code = d
    pred = 1 if stat == pred_code else 0
    print(f"{cli_id} {endpoint} {stat} {pred}")