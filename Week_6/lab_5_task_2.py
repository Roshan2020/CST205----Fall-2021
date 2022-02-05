from PIL import Image

source = Image.open('images/elephant.jpg')
img = Image.open('images/bunny.jpg')
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

#img = Image.new('RGB', (100, 100), 'red')

# img1 tranform
a = 1
b = 0
c = 10 #left/right (i.e. 5/-5)
d = 0
e = 1
f = 10 #up/down (i.e. 5/-5)
source = source.transform(source.size, Image.AFFINE, (a, b, c, d, e, f))

pic = blending(source, target)
img = img.resize((img.width//2, img.height//2))
pic = blending(img, pic)
pic.show()