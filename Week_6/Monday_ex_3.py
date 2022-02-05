from PIL import Image

source = Image.open('images/elephant.jpg')
img = Image.open('images/bunny.jpg')
#img = img.resize((img.width//6, img.height//6))

new_w, new_h = source.width+800,source.height+200
new1_w, new1_h = img.width+100,img.height+200

target = Image.new('RGB', (new_w, new_h), 'white')

target_x = 100
for source_x in range(source.width):
  target_y = 100
  for source_y in range(source.height):
    pixel = source.getpixel((source_x, source_y))
    target.putpixel((target_x, target_y), pixel)
    target_y += 1
  target_x += 1

#target = Image.new('RGB', (new1_w, new1_h), 'white')

target_x = 100
for img_x in range(img.width):
  target_y = 100
  for img_y in range(img.height):
    pixel = img.getpixel((img_x, img_y))
    target.putpixel((target_x, target_y), pixel)
    target_y += 1
  target_x += 1

target.show()