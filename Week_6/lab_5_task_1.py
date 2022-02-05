from PIL import Image
im1 = Image.open('images/sun_beach.jpg')

def reduce_green_and_blue(picture):
    new_list=[]
    for p in picture.getdata():
        new_list.append((p[0], int(p[1]*.7), int(p[2]*.7)))
    picture.putdata(new_list)
    picture.show()

reduce_green_and_blue(im1)