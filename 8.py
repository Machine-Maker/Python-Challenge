# working hard?
from urllib.request import urlopen
from bz2 import decompress

page_content = urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read().decode('unicode-escape')

un = page_content.split("un: '")[1].split("'\n")[0]
pw = page_content.split("pw: '")[1].split("'\n")[0]

print('Username:', decompress(bytes(un, 'ISO-8859-1')).decode('ISO-8859-1'))
print('Password:', decompress(bytes(pw, 'ISO-8859-1')).decode('ISO-8859-1'))

# Username: 'huge'
# Password: 'file'


# http://www.pythonchallenge.com/pc/def/integrity.html
