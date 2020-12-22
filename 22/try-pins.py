#!/usr/bin/env python3

from pwn import process, asm, ELF, context
from multiprocessing import Process
from numpy import array_split

context.log_level = 'error'

elf = ELF('./padawanlock')

assembly_for_h = asm('mov byte ptr [ebx], 0x48') # Instruction that adds H to the output - must be our entrypoint

def brute_force_range(search, pid):
    # Reversing the caculation
    # 0x124B base address of jump table
    # 13 byte difference between the address to which we jump and the instruction that appends the char
    # address = base + (20 * input)
    # address - base = 20 * input
    # (address - base) / 20 = input
    base = 0x124b
    count = 0

    with open(f"results_{pid}.txt", "w") as output_file:
        for result in search:
            address = result - 13
            input = (address - base) / 20
            input = round(input)
            p = process("./padawanlock")
            p.sendline(str(input))
            output = p.recvall().decode('ascii')
            flag = output.split('Unlocked secret is:')[1].strip()

            if not flag.startswith("H"):
                output_file.write(f"Error: Invalid flag {flag} for input {input}\n")

            output_file.write(f"{flag} for {input}\n")

            if "HV20" in flag:
                print(flag + " " + pid)
                exit(0)
            
            count += 1
            if count % 100 == 0:
                print(f"HV PID {pid} has {count}/{len(search)}")


search = list(elf.search(assembly_for_h))
a, b, c, d = array_split(search, 4)

p1 = Process(target=lambda: brute_force_range(a, "1"))
p2 = Process(target=lambda: brute_force_range(b, "2"))
p3 = Process(target=lambda: brute_force_range(c, "3"))
p4 = Process(target=lambda: brute_force_range(d, "4"))

p1.start()
p2.start()
p3.start()
p4.start()
