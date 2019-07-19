# peak hill
from pickle import load
from urllib.request import urlopen
from os.path import exists
from os import makedirs

makedirs('5', exist_ok=True)
if not exists('5/banner.p'):
    page_content = urlopen('http://www.pythonchallenge.com/pc/def/banner.p').read()
    with open('5/banner.p', 'wb') as banner_file:
        banner_file.write(page_content)
        print('Created banner.p file')

with open('5/banner.p', 'rb') as pickle_data:
    data = load(pickle_data)

for r in data:
    for t in r:
        print(t[0]*t[1], end="")
    print('')

# channel


# http://www.pythonchallenge.com/pc/def/peak.html
