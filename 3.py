# re
from re import findall
from urllib.request import urlopen
from os.path import exists
from os import makedirs

makedirs('3', exist_ok=True)

if not exists('3/mess.txt'):
    page_content = urlopen('http://www.pythonchallenge.com/pc/def/equality.html').read().decode('utf-8')
    mess = page_content.split('<!--')[1].split('-->')[0]
    with open('3/mess.txt', 'w') as mess_file:
        mess_file.write(mess)
        print('Created mess.txt file')


with open('3/mess.txt', 'r') as char_file:
    chars = char_file.read()

regex = findall(r'[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]', chars)

print('Answer:', "".join(s[4] for s in regex))

# linkedlist

# http://www.pythonchallenge.com/pc/def/equality.html
