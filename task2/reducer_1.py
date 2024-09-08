#!/usr/bin/env python3
import sys
def reducer1():
    for line in sys.stdin:
        d = line.strip().split(" ")
        if len(d) == 5:
            x = f"{d[3]} {' '.join(d[:3] + d[4:])} {pred}"
            print(x)
        elif len(d) == 2:
            req_id, pred = d
            
if __name__ == "__main__":
    reducer1()