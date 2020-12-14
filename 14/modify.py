#!/usr/bin/env python3

data = []
with open('./5625d5bc-ea69-433d-8b5e-5a39f4ce5b7c.gif', 'rb') as input_file:
    data = input_file.read()

xor_key = b'\x55\xaa' # trailing data
xor_key = b'\xeb\x2e' # exif comment
data = bytearray(data)

for i in range(len(data)):
    key = xor_key[0] if i % 2 == 0 else xor_key[1]
    data[i] ^= key

with open('./test.bin', 'wb') as output_file:
    output_file.write(data)