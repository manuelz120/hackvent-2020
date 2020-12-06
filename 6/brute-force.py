#!/usr/bin/env python3

from pyzbar.pyzbar import decode
from PIL import Image

output = decode(Image.open('./solved.bmp'))

flag = output[0].data.decode('ascii')

print(flag)

def concat_images_horizontally(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

def concat_images_vertically(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

for i in range(1, 7):
    top_left = Image.open(f"parts/{i}-top-left.jpg")
    top_right = Image.open(f"parts/{i}-top-right.jpg")
    bottom_left = Image.open(f"parts/{i}-bottom-left.jpg")
    bottom_right = Image.open(f"parts/{i}-bottom-right.jpg")

    top = concat_images_horizontally(top_left, top_right)
    bottom = concat_images_horizontally(bottom_left, bottom_right)
    full = concat_images_vertically(top, bottom)

    for j in range(4):
        full = full.transpose(Image.ROTATE_90)
        full.save(f"./out/{i}_{j}.jpg")

        output = decode(full)
        print(output)