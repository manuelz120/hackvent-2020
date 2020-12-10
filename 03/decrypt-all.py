#!/usr/bin/env python3
from os import system
from base64 import b64decode

key = "2445b967 cfb14967 dceb769b"

for i in range(0, 100):
    filename = f"{i}.bin".rjust(8, "0")

    system(f"./bkcrack-1.0.0-Linux/bkcrack -P ./790ccd6f-cd84-452c-8bee-7aae5dfe2610.zip -C ./941fdd96-3585-4fca-a2dd-e8add81f24a1.zip -c {filename} -k {key} -d ./temp.bin")
    system(f"./bkcrack-1.0.0-Linux/tools/inflate.py < ./temp.bin > encrypted/{filename}")

    with open(f"./encrypted/{filename}", "rb") as file:
        content = file.read().decode('utf-8')
        output = b64decode(content)
        if b"HV20" in output:
            print(output)
            break
