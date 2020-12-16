#!/usr/bin/env python3
from itertools import product, permutations
from rubik.cube import Cube
from re import compile

flag_regex = compile('^HV20{[a-z3-7_@]+}$')

def get_flag_from_qube(cube: Cube):
    cube_string = str(cube)
    lines = list(map(lambda s: s.replace(" ", ""), cube_string.splitlines()))

    top = lines[0] + lines[1] + lines[2]
    left = lines[3][0:3] + lines[4][0:3] + lines[5][0:3]
    middle = lines[3][3:6] + lines[4][3:6] + lines[5][3:6]
    right = lines[3][6:9] + lines[4][6:9] + lines[5][6:9]
    rightmost = lines[3][9:12] + lines[4][9:12] + lines[5][9:12]
    bottom = lines[6] + lines[7] + lines[8]

    parts = [top, left, middle, right, rightmost, bottom]

    for a, b, c, d, e, f in permutations(parts):
        flag = a + b + c + d + e + f
        if flag.startswith("HV20{") and flag.endswith("}"):
            with open('flag.txt', 'a+') as out_file:
                if flag_regex.match(flag):
                    print(flag)
                out_file.write(flag + "\n")

number_of_moves = 5
moves = "L Li R Ri U Ui D Di F Fi B Bi".split(' ')

# for sequence in product(moves, repeat=number_of_moves):
#     c = Cube("6_ei{aes3HV7_weo@sislh_e0k__t_nsooa_cda4r52c__nsllt}ph")
#     move = " ".join(sequence)
#     c.sequence(move)
#     get_flag_from_qube(c)

for m1 in moves:
    for m2 in moves:
        for m3 in moves:
            for m4 in moves:
                for m5 in moves:
                    for m6 in moves:
                        c = Cube("6_ei{aes3HV7_weo@sislh_e0k__t_nsooa_cda4r52c__nsllt}ph")
                        move = f"{m1} {m2} {m3} {m4} {m5} {m6}"
                        c.sequence(move)
                        get_flag_from_qube(c)