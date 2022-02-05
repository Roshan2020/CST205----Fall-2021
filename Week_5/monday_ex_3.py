from PIL import Image
im2 = Image.open('larrys_place.png')

negative_list = [(255-p[0], 255-p[1], 255-p[2]) 
                        for p in im2.getdata()]
im2.putdata(negative_list)
im2.show()