#!/usr/bin/env python3
from itertools import permutations

middle_parts = ["Petrus_is", "_Valid.", "Rubik_would", "_be_proud."]

start = "HV20{Erno_"
end = "#HV20QRubicsChal}"

for (part1, part2, part3, part4) in permutations(middle_parts):
    flag = start +  part1 + part2 + part3 + part4 + end
    print(flag)

# HV20{Erno_Rubik_would_be_proud.Petrus_is_Valid.#HV20QRubicsChal}