#!/usr/bin/env python3
from os import system
from shlex import quote

key = b'\x1f\x9d\x8c\x42\x9a\x38\x41\x24\x01\x80\x41\x83\x8a\x0e\xf2\x39\x78\x42\x80\xc1\x86\x06\x03\x00\x00\x01\x60\xc0\x41\x62\x87\x0a\x1e\xdc\xc8\x71\x23'

with open('./test1.z', 'wb') as file:
    file.write(key)

# data = b''

# with open('./5862be5b-7fa7-4ef4-b792-fa63b1e385b7.xls_part9', 'r') as input_file:
#     lines = input_file.readlines()
#     for line in lines:
#         data += bytes.fromhex(line.strip())

# with open('./test-large.bin', 'wb') as file:
#     file.write(data)

des_algorithms = list(filter(len, map(lambda s: s.strip(), 
    """des               des-cbc           des-cfb           
       des-ecb           des-ede           des-ede-cbc       des-ede-cfb       
       des-ede-ofb       des-ede3          des-ede3-cbc      des-ede3-cfb      
       des-ede3-ofb      des-ofb           des3              desx""".split(' '))))

print(des_algorithms)
count = 0

for algo in des_algorithms:
    k = quote(str(key[:8])[2:-1])
    s = quote(str(key[8:])[2:-1])
    print(algo)
    #system(f"openssl enc -{algo} -salt -in encrypted-file -out flag -d -K {k} -S {s}")
    system(f"rm flag")
    #system(f"openssl enc -{algo} -salt -in encrypted-file -out flag -d -K {k} -S {s}")
    system(f"openssl enc -{algo} -salt -in encrypted-file -out flag -d -pass file:test1.z")
    #system(f"openssl enc -{algo} -salt -in encrypted-file -out flag -d -pass pass:1f9d8c429a384124018041838a0ef239784280c186060300000160c04162870a1edcc87123")
    system(f"file ./flag")
    system(f"cp test1 test/{count}.bmp")
    system(f"cat flag >> test/{count}.bmp")
    count += 1
    print("--------------------------")

