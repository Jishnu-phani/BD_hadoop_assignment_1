#!/usr/bin/env python
import sys

def reducer3():
    current_id = None
    cost = 0
    pos = 0
    tot = 0
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()
        client_id, success, price = parts
        if current_id is None:
            current_id = client_id
        if current_id != client_id:
            print(f"{current_id} {pos}/{tot} {cost}")
            current_id = client_id
            cost = 0
            pos = 0
            tot = 0
        if success == '1':
            cost += int(price)
            pos += 1
        tot += 1
    print(f"{current_id} {pos}/{tot} {cost}")
        
if __name__ == "__main__":
    reducer3()