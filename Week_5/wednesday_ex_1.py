
from PIL import Image

im = Image.open('images/rubble.jpg')

def sepia(pixel):
    if pixel[0] < 63:
        r,g,b = int(pixel[0]*1.1), pixel[1], int(pixel[2]*.9)
    elif pixel[0]>62 and pixel[0]<192:
        r,g,b = int(pixel[0]*1.15), pixel[1], int(pixel[2]*.85)
    else:
        r = int(pixel[0]*1.08)
        if r>255: r=255
        g,b = pixel[1], pixel[2]//2  
    return r,g,b

# sepia_list = map(sepia, im.getdata())
sepia_list = [sepia(p) for p in im.getdata()]

im.putdata(list(sepia_list))

im.show()
# im.save()