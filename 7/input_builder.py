#!/usr/bin/env python3

first = "BumBumWithTheTumTum"
first = "_B_u_m_B_u_m_W_i_t_h_T_h_e_T_u_m_T_u_m"
second = "htroFdnAkcaB" # BackAndForth reversed
third = "nOMNSaSFjC["

def unscramble_first(input):
    input_length = len(input)
    output = ""
    for i in range(input_length):
        # if i % 2 == 0 and i <= input_length:
        #     output += input[]

    return output

# byte num = 42;
#         for (int index = 0; index < charArray3.Length; ++index)
#         {
#           char ch = (char) ((uint) charArray3[index] ^ (uint) num);
#           num = (byte) ((int) num + index - 4);
#           str4 += ch.ToString();
#         }

def unscramble_third(input):
    key = 42
    output = ""

    for i in range(len(input)):
        ch = chr(ord(input[i]) ^ key)
        key += i - 4
        output += ch

    return output

print(unscramble_third("DinosAreLit"))

# HV20{r3?3rs3_3ng1n33r1ng_m4d3_34sy}