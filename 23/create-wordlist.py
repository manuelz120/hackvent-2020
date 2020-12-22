#!/usr/bin/env python3

with open('keys.txt', 'w') as output_file:
    for i in range(20000000, 300000000):
        output_file.write(f"{i}\n")
    