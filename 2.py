# ocr
from urllib.request import urlopen
from os.path import exists
from os import makedirs

makedirs('2', exist_ok=True)

if not exists('2/mess.txt'):
    page_content = urlopen('http://www.pythonchallenge.com/pc/def/ocr.html').read().decode('utf-8')
    mess = page_content.split('<!--')[2].split('-->')[0]
    with open('2/mess.txt', 'w') as mess_file:
        mess_file.write(mess)
        print('Created mess.txt file')


with open('2/mess.txt', 'r') as char_file:
    chars = char_file.read()

counts = {}

for c in chars:
    counts[c] = counts.get(c, 0) + 1

print('Answer:', "".join([c for c in counts.keys() if counts[c] == 1]))

# equality

# http://www.pythonchallenge.com/pc/def/ocr.html
