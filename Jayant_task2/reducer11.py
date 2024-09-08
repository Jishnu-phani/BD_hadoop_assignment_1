#!/usr/bin/env python3
import sys
client_time_req = {}
client_time_server = {}
for line in sys.stdin:
    d = line.strip().split(" ")
    if len(d) == 6:
        timestamp, req_id, c_id, endpoint, broken, stat = d
        try: #handled
            broken = float(broken)
        except ValueError:
            continue
        if timestamp not in client_time_req:
            client_time_req[timestamp] = set()
        if c_id in client_time_req[timestamp]:
            # print(f"{req_id} {c_id} {endpoint} '500'")
            continue #handled
        client_time_req[timestamp].add(c_id)
        if timestamp not in client_time_server:
            client_time_server[timestamp] = {}
        if endpoint not in client_time_server[timestamp]:
            client_time_server[timestamp][endpoint] = {"broken": broken}
        if client_time_server[timestamp][endpoint]["broken"] < 3:
            client_time_server[timestamp][endpoint]["broken"] += 1
            print(f"{req_id} {c_id} {endpoint} 200")
        else:
            print(f"{req_id} {c_id} {endpoint} 500")
    elif len(d) == 2:
        req_id, pred = d
        # print(f"{x} {y}")
        print(f"{req_id} {pred}")
