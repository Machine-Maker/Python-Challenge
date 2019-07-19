# now there are pairs
from re import findall
from urllib.request import urlopen
from zipfile import ZipFile
from os.path import exists
from os import makedirs
from sys import exit

makedirs('6', exist_ok=True)
if not exists('6/channel.zip'):
    zip_page = urlopen('http://www.pythonchallenge.com/pc/def/channel.zip').read()
    with open('6/channel.zip', 'wb') as zip_file:
        zip_file.write(zip_page)
        print('Created channel.zip file')

unzipped = ZipFile('6/channel.zip')
comments = []
number = "90052"

while True:
    with unzipped.open(number + '.txt') as num_file:
        file_content = num_file.read().decode('utf-8')
    number = file_content.split()[-1]
    if not number.isdigit():
        break
    else:
        comments.append(unzipped.getinfo(number + '.txt').comment.decode('utf-8'))

print("".join(comments))

# HOCKEY

# oxygen (Hockey is spelled with oxygen)


# http://www.pythonchallenge.com/pc/def/channel.html
