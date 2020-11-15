from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import cv2

# in_file, out_file, text = sys.argv[1:]
text = 'Mr. Sachin Chauhan'
in_file = 'certi.jpg'
out_folder = 'out'

names = []
f = open('names', 'r')
for line in f:
    names.append(line.strip())
f.close()
print(names)

im = cv2.imread(in_file)
print(im.shape)
font_path = "/Library/Fonts/Arial Unicode.ttf"
font = ImageFont.truetype(font_path, 30)

for name in names:
    img = Image.open(in_file)
    draw = ImageDraw.Draw(img)
    draw.text((390, 295), name, font=font, fill=(0,0,0))
    img.save(out_folder + '/' + name + '_certi.jpg')
