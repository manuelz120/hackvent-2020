#!/usr/bin/python3

first = "CTGTCGCGAGCGGATACATTCAAACAATCCTGGGTACAAAGAATAAAACCTGGGCAATAATTCACCCAAACAAGGAAAGTAGCGAAAAAGTTCCAGAGGCCAAA" # 00
second = "ATATATAAACCAGTTAATCAATATCTCTATATGCTTATATGTCTCGTCCGTCTACGCACCTAATATAACGTCCATGCGTCACCCCTAGACTAATTACCTCATTC" # 11

nibbles = ["00", "01", "10", "11"]
bases = ["A", "C", "G", "T"]

first_bitstream = ""
second_bitstream = ""

for (a, b) in zip(first, second):
    index_a = bases.index(a)
    index_b = bases.index(b)
    first_bitstream += nibbles[index_a]
    second_bitstream += nibbles[index_b]

first_bytes = [first_bitstream[i:i+8] for i in range(0, len(first_bitstream), 8)]
second_bytes = [second_bitstream[i:i+8] for i in range(0, len(second_bitstream), 8)]

flag = ""

for (byte1, byte2) in zip(first_bytes, second_bytes):
    char = chr(int(byte1, 2) ^ int(byte2, 2))
    flag += char

print(flag) # HV20{s4m3s4m3bu7diff3r3nt}
