#!/usr/bin/env python3

from pyzbar.pyzbar import decode
from PIL import Image
from itertools import count, permutations

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

top_left_parts = list(map(lambda x: Image.open(f"parts/{x}-top-left.jpg"), range(1, 22)))
top_right_parts = list(map(lambda x: Image.open(f"parts/{x}-top-right.jpg"), range(1, 22)))
bottom_left_parts = list(map(lambda x: Image.open(f"parts/{x}-bottom-left.jpg"), range(1, 22)))
bottom_right_parts = list(map(lambda x: Image.open(f"parts/{x}-bottom-right.jpg"), range(1, 22)))

def get_filename_from_pil_image(image):
    return image.filename.split('/')[1].split('.')[0]

counter = 0
for top_left in top_left_parts:
    print(counter)
    for top_right in top_right_parts:
        for bottom_left in bottom_left_parts:
            for bottom_right in bottom_right_parts:
                top = concat_images_horizontally(top_left, top_right)
                bottom = concat_images_horizontally(bottom_left, bottom_right)
                full = concat_images_vertically(top, bottom)

                for j in range(4):
                    full = full.transpose(Image.ROTATE_90)
                    output = decode(full)
                    if len(output) > 0:
                        full.save(f"./out/{get_filename_from_pil_image(top_left)}_{get_filename_from_pil_image(top_right)}_{get_filename_from_pil_image(bottom_left)}_{get_filename_from_pil_image(bottom_right)}_{j}.jpg")
                        print(output)

    counter += 1



# counter = 6

# for top_left_part in top_left_parts:
#     rotated_versions = ["bottom-left", "bottom-right", "top-right"]
#     for rotation in rotated_versions:
#         counter += 1
#         top_left_part = top_left_part.transpose(Image.ROTATE_90)
#         top_left_part.save(f"parts/{counter}-{rotation}.jpg")

# counter = 6

# for top_right_part in top_right_parts:
#     rotated_versions = ["top-left", "bottom-left", "bottom-right"]
#     for rotation in rotated_versions:
#         counter += 1
#         top_right_part = top_right_part.transpose(Image.ROTATE_90)
#         top_right_part.save(f"parts/{counter}-{rotation}.jpg")

# counter = 6

# for bottom_left_part in bottom_left_parts:
#     rotated_versions = ["bottom-right", "top-right", "top-left"]
#     for rotation in rotated_versions:
#         counter += 1
#         bottom_left_part = bottom_left_part.transpose(Image.ROTATE_90)
#         bottom_left_part.save(f"parts/{counter}-{rotation}.jpg")

# counter = 6

# for bottom_right_part in bottom_right_parts:
#     rotated_versions = ["top-right", "top-left", "bottom-left"]
#     for rotation in rotated_versions:
#         counter += 1
#         bottom_right_part = bottom_right_part.transpose(Image.ROTATE_90)
#         bottom_right_part.save(f"parts/{counter}-{rotation}.jpg")

# all_parts = top_left_parts + top_right_parts + bottom_left_parts + bottom_right_parts
# possible_squares = list(permutations(all_parts, 4))
# print(f"Got {len(possible_squares)} possibilities")

# counter = 0

# for (top_left, top_right, bottom_left, bottom_right) in possible_squares:
#     top = concat_images_horizontally(top_left, top_right)
#     bottom = concat_images_horizontally(bottom_left, bottom_right)
#     full = concat_images_vertically(top, bottom)
#     counter += 1

#     for j in range(4):
#         full = full.transpose(Image.ROTATE_90)
#         output = decode(full)
#         if len(output) > 0:
#             full.save(f"./out/{get_filename_from_pil_image(top_left)}_{get_filename_from_pil_image(top_right)}_{get_filename_from_pil_image(bottom_left)}_{get_filename_from_pil_image(bottom_right)}_{j}.jpg")
#             print(output)

#     if counter % 1000 == 0:
#         print(counter)
