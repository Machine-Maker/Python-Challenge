# What about making trans?
from string import ascii_lowercase
from urllib.request import urlopen

page_content = urlopen('http://www.pythonchallenge.com/pc/def/map.html').read().decode('utf-8')

text = page_content.split('#f000f0">\n')[1].split('\n')[0]

intab = ascii_lowercase[-2:] + ascii_lowercase[:-2]

trans = str.maketrans(intab, ascii_lowercase)

print(text.translate(trans))

# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

print("map".translate(trans))

# http://www.pythonchallenge.com/pc/def/map.html
