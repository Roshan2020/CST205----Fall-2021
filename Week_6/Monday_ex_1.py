# This code is about blending two different imgs into one img
from PIL import Image
source = Image.open('images/jeanne_small.jpg')
target = Image.open('images/beach.jpg')

source = source.resize((target.width, target.height))

w,h = source.width, source.height

x_shift = 240
y_shift = 200

for src_x, trg_x in enumerate(range(w)):
  for src_y, trg_y in enumerate(range(h)):
    r_s, g_s, b_s = source.getpixel((src_x, src_y))
    r_t, g_t, b_t = target.getpixel((trg_x, trg_y))

    blend = ( (r_s+r_t)//2, (g_s+g_t//2), (b_s+b_t)//2 )

    target.putpixel((trg_x, trg_y), blend)
 
target.show()