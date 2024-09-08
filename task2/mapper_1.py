#!/usr/bin/env python3
import sys
def mapper1():
    for line in sys.stdin:
        parts = line.strip().split()
        if len(parts) == 4:  # This is request info
            servers_down = 0.0
            request_id, client_id, endpoint, timestamp = parts
            print(f"{request_id} {client_id} {endpoint} {timestamp} {servers_down}")
        elif len(parts) == 5:
            request_id, client_id, endpoint, timestamp, servers_down = parts
            print(f"{request_id} {client_id} {endpoint} {timestamp} {servers_down}")
        elif len(parts) == 2:  # This is predicted status code info
            request_id, predicted_code = parts
            print(f"{request_id} {predicted_code}")
            
if __name__ == "__main__":
    mapper1()   