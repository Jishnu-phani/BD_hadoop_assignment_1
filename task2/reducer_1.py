#!/usr/bin/env python
import sys
def reducer1():
    previous_line = None

    for line in sys.stdin:
        line = line.strip()
        
        if previous_line is None:
            previous_line = line
        else:
            # Extract the value from the previous line
            previous_parts = previous_line.split()
            current_parts = line.split()
            
            # Extract the timestamp from the current line
            timestamp = current_parts[3]
            
            # Combine the timestamp, current line (excluding the timestamp), and the value from the previous line
            combined_line = f"{timestamp} {' '.join(current_parts[:3] + current_parts[4:])} {previous_parts[1]}"
            print(combined_line)
            
            # Reset previous_line to None to read the next pair of lines
            previous_line = None
            
if __name__ == "__main__":
    reducer1()