# HV20.16 Naughty Rudolph

For this challenge, we get a 3D model (STL file) of a 3x3 rubics code. Instead of colors, each side of the cube is covered by characters that probably form the flag. Using an STL viewer (e.g. Paint 3D) I created a flat list of the characters on each side of the list. This turned out quite tricky, since some of the characters are rotated which leeds to ambiguity (e.g. `l` vs `1` or `d` vs `p`). From the hints we already know that it takes approximately 5 steps to solve the cube and get the flag. Moreover, the hints also mention on how we need to read the tiles to get the flag and specify a regex (`^HV20{[a-z3-7_@]+}$`) which matches the solution.

Using all this information and a small python package (https://pypi.org/project/rubik-cube/), I wrote a [primitive script](./brute-force.py) that brute forces all possible sequences of 5 moves and searches the outsides of the cube to find a valid flag. After a couple of minutes, the program produced a number of possible flags. I manually looked over the output and tried to submit the most plausible one:

**Flag:** HV20{no_sle3p_since_4wks_lead5_to\*@\_hi6hscore_a7_last}
