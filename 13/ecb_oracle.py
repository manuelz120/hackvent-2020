#!/usr/bin/env python

from Crypto.Cipher import AES
import sys

def split_len(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def oracle(chosen):
    secret = "foobarbaz1234567890%sSecret42" % chosen # target to decrypt
    secret = getPadding(secret)
    if display:
        displaySecret(secret) # For illustrative purposes
    ct = cipher.encrypt(secret)
    return ct

def getPadding(secret):
    pl = len(secret)
    mod = pl % 16
    if mod != 0:
        padding = 16 - mod
        secret += "X" * padding
    return secret

def displaySecret(secret):
    split = split_len(secret, 16)
    display = ""
    for i in split:
        for j in split_len(i, 1):
            display += j + " "
        display += " "

    print "pt: %s" % display

def displayCiphertext(ct):
    split = split_len(ct, 16)
    display = ""

    for i in split:
        display += i.encode('hex') + " "

    print "ct: %s" % (display)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit("Usage: %s plaintext" % sys.argv[0])

    display=True # Toggle for verbose out put
    key = "deadbeefcafecode"
    cipher = AES.new(key, AES.MODE_ECB, "\x00" * 16)
    cipher.block_size=8

    chosen = sys.argv[1]
    ct = oracle(chosen)
    if display:
        displayCiphertext(ct)
    else:
        print ct.encode('hex')