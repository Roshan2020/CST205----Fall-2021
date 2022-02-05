from PIL import Image
import glob

##############################################################
# Function
# Input: the median pixel of all images from each coordinate
# Output: creates a new image named 'output.png'
##############################################################
def img_median(img):
    new_img = Image.new('RGB', (img[0].width, img[0].height))

    # Loop to create a img by locating the median for each pixel value
    # and placing it the blank img file
    for x in range (img[0].width):
        for y in range (img[0].height):
            pixels = []
            for z in range(len(img)):
                pixels.append(img[z].getpixel((x, y)))
            red_pixels = sorted(pixels, key=lambda col: col[0])
            green_pixels = sorted(pixels, key=lambda col:col[1])
            blue_pixels = sorted(pixels, key=lambda col:col[2])
            median = int((len(pixels) + 1) / 2) - 1
            new_img.putpixel((x, y), (red_pixels[median][0], green_pixels[median][1], blue_pixels[median][2]))
    new_img.save('output.png')

image_files = []

for image in glob.glob('hw2_images/*.png'):
    image_files.append(Image.open(image))

img_median(image_files)