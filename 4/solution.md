# HV20.04 Br❤️celet

This challenge was quite different. From the challenge description we know that the flag must be encoded in the colors of the pearls. Moreover, we know that violet acts as a delimiter and binary encoding was used. Apart from violet, there are four colors: magenta, green, blue and yellow. Assuming that the flag is in the normal ASCII range (8 bit), my first guess was to map those colors to the different powers of 2: `0001, 0010, 0100, 1000`. Multiple colors within a single section can be combined using XOR. Combining two sections would give us one byte, which hopefully corresponds to a character of the flag. 

As we don't know the exact mapping, I wrote a small program that brute forces all possible combinations and checks which one decodes to a valid flag. Moreover, I had to account for the empty section (two violet pearls) by mapping it to the sequence `0000`. The final [program](./crack.py) looks as follows:

```python
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
```

**Flag:** HV20{Ilov3y0uS4n74}
