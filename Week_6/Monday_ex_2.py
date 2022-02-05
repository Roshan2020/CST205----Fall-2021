from PIL import Image
import math

def color_distance(c1, c2):
    val = 0
    for i in range(3):
        val += math.pow((c1[i]- c2[i]), 2)
    return math.sqrt(val)

def chromakey(src, bg, refp):
    for x in range(src.width):
        for y in range(src.height):
            cur_pixel = src.getpixel((x,y))

            if color_distance(cur_pixel, refp) < 150:
                src.putpixel((x,y), bg.getpixel((x,y)))
        
    return src


bg = Image.open('images/rubble.jpg')
lad = Image.open('images/lad.jpg')
bg = bg.resize((lad.width, lad.height))
lad_blue = lad.getpixel((50,130))
chromakey(lad, bg, lad_blue)

lad.show()