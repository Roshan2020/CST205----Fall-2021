from PIL import Image
im2 = Image.open('larrys_place.png')
#im2.show()
def reduce_red(picture):
    new_list=[]
    for p in picture.getdata():
        new_list.append((p[0]//2, p[1], p[2]))
    picture.putdata(new_list)
    picture.show()

reduce_red(im2)