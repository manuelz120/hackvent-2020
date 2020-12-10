#!/usr/bin/env python3
from itertools import permutations


bracelet = list(filter(len, "G_MY_GB_MG_GB_MGBY_GBY_GB_BY_BY_GBY_MY_BY_?_GBY_GY_GY_BY_BY_G_GB_MGB_BY_GBY_BY_G".split("_")))
nibbles = list(map(lambda x: int(x, 2), ["1000", "0100", "0010", "0001"]))
colors = ["G", "M", "Y", "B"]

for nibble_order in permutations(nibbles):
    for color_order in permutations(colors):
        output = ""

        for entry in bracelet:
            number = 0
            for char in entry:
                try:
                    index = color_order.index(char)
                    number ^= nibble_order[index]
                except ValueError:
                    break

            output += '{0:04b}'.format(number)

        flag = ""
        try:
            chunks = [output[i:i+8] for i in range(0, len(output), 8)]
            for bit in chunks:
                value = int(bit, 2)
                flag += chr(value)
            
            if flag.isprintable():
                print(flag)
        except UnicodeDecodeError:
            pass
