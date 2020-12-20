#!/usr/bin/env python3

seven_zip_magic = [ord('7'), ord('z'), 0xBC, 0xAF, 0x27, 0x1C]
key = list(map(ord, "Rabbits are small mammals in the family Leporidae of the order Lagomorpha (along with the hare and the pika). Oryctolagus cuniculus includes the European rabbit species and its descendants, the world's 305 breeds[1] of domestic rabbit. Sylvilagus includes 13 wild rabbit species, among them the seven types of cottontail. The European rabbit, which has been introduced on every continent except Antarctica, is familiar throughout the world as a wild prey animal and as a domesticated form of livestock and pet. With its widespread effect on ecologies and cultures, the rabbit (or bunny) is, in many areas of the world, a part of daily life-as food, clothing, a companion, and a source of artistic inspiration."))

for c, k in zip(seven_zip_magic, key):
    print("%x" % (c ^ k))