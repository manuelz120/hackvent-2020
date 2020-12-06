#!/usr/bin/env python3

from pyzbar.pyzbar import decode
from PIL import Image

output = decode(Image.open('./solved.bmp'))

flag = output[0].data.decode('ascii')

print(flag)