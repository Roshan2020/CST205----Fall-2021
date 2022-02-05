from PIL import Image, ImageDraw

import random


# Generate a dark 8-bit color

my_color = random.randint(0, 150)


# Enter your name here as a string

my_name = "Roshan Indika Menik Arachchi Menik Arachchige "


# Create 8-bit grayscale image of size 200x200 using

# the randomly-generated 8-bit color

img = Image.new('L', (200,200), color = my_color)


# add text to drawing at position (30,30)

# in white

my_text = ImageDraw.Draw(img)

my_text.text((30, 30), my_name, fill=255)


# show image using default system viewer

img.show()