#!/usr/bin/env python3
import sys
def reducer1():
    previous_line = None

    for line in sys.stdin:
        line = line.strip()
        
        if previous_line is None:
            previous_line = line
        else:
            previous_parts = previous_line.split()
            current_parts = line.split()
            
            timestamp = current_parts[3]
            
            combined_line = f"{timestamp} {' '.join(current_parts[:3] + current_parts[4:])} {previous_parts[1]}"
            print(combined_line)
            
            previous_line = None
            
if __name__ == "__main__":
    reducer1()