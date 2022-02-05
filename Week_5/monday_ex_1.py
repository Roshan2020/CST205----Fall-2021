from PIL import Image # an error here means that Pillow is not installed
from pprint import pprint
im1 = Image.open('larrys_place.jpg')
pixel_list = im1.getdata()
print(f'The number of pixels is {len(pixel_list)}.')
# print(list(pixel_list))
pprint(list(pixel_list))