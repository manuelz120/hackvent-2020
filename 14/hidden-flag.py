#!/usr/bin/env python3

part1 = None
part2 = None

with open('c.img', 'rb') as input_file:
    input_file.seek(0xF4)
    part1 = input_file.read(29)
    input_file.seek(0x9e)
    part2 = input_file.read(29)

out = ""

for p1, p2 in zip(part1, part2):
    out += chr(p1 ^ p2)

print(out)
# HV20{h1dd3n-1n-pl41n-516h7}
