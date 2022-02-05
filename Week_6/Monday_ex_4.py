from PIL import Image

source = Image.open('images/elephant.jpg')
img = Image.open('images/squirrel.jpg')
target = Image.open('images/photo_frame.jpg')
white = Image.open('images/white.jpg')


def blending(source, target):
    x_shift = target.width//2 - 100
    y_shift = target.height//2

    source_x=0
    for x in range(x_shift, x_shift+source.width):
        source_y=0
        for y in range(y_shift, y_shift+source.height):
            r_s, g_s, b_s = source.getpixel((source_x, source_y))
            r_t, g_t, b_t = target.getpixel((x, y))

            blend = ( (r_s+r_t)//2, (g_s+g_t)//2, (b_s+b_t)//2 )

            target.putpixel((x,y), blend)
            source_y += 1
        source_x += 1
    return target

pic = blending(source, white)
#img = img.resize((img.width//2, img.height//2))
#pic = blending(img, pic)
pic.show()