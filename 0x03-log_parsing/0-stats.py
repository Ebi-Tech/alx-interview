#!/usr/bin/python3
'''This script reads stdin line by line and computes metrics'''

import sys
import signal

# Define the signal handler for CTRL + C
def signal_handler(sig, frame):
    print_metrics()
    sys.exit(0)

# Define a dictionary to store the count of each status code
status_code_count = {}

# Define a variable to store the total file size
total_file_size = 0

# Define a function to print the metrics
def print_metrics():
    print(f"Total file size: {total_file_size}")
    for status_code in sorted(status_code_count.keys()):
        print(f"{status_code}: {status_code_count[status_code]}")

# Set the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read stdin line by line
line_count = 0
for line in sys.stdin:
    line_count += 1
    try:
        # Parse the line and extract the file size and status code
        parts = line.split()
        file_size = int(parts[-1])
        status_code = int(parts[-2])

        # Update the total file size
        total_file_size += file_size

        # Update the status code count
        if status_code in status_code_count:
            status_code_count[status_code] += 1
        else:
            status_code_count[status_code] = 1

        # Print the metrics every 10 lines
        if line_count % 10 == 0:
            print_metrics()

    except:
        # Skip lines that don't match the input format
        continue
