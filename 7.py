# smarty
from urllib.request import urlopen
from os.path import exists
from os import makedirs
from PIL import Image
from re import findall

makedirs('7', exist_ok=True)
if not exists('7/oxygen.png'):
    image = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png").read()
    with open('7/oxygen.png', 'wb') as image_file:
        image_file.write(image)
        print('Created oxygen.png file')

image = Image.open('7/oxygen.png')

s = ""

y = 43
for j in range(0, 608, 7):
    pixel = image.getpixel((j, y))
    if pixel[3] is 255:
        s += chr(pixel[0])

print('Answer:', "".join([chr(int(c)) for c in findall(r'\d+', s)]))

# integrity
# http://www.pythonchallenge.com/pc/def/oxygen.html
