from PIL import Image # an error here means that Pillow is not installed
im = Image.open('steglitz.jpg') 
# print(im)
print(im.size)
width, height = im.size

pic_width = 4 
pic_height = 5 
for x in range(pic_width): # loop from 0 to pic_width -1
    for y in range(pic_height): # loop from 0 to pic_height -1
        print((x,y))