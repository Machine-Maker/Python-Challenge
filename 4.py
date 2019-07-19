# follow the chain
from urllib.request import urlopen
from re import findall

base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

num = "12345"

count = 400
while count >= 0:
    url_data = str(urlopen(base_url + num).read())
    if num == "16044":
        num = str(int(int(num)/2))
    else:
        matches = findall(r'(\d{5}|\d{4}|\d{3})', url_data)
        if len(matches) == 0:
            print('Something happened!')
            break
        else:
            num = findall(r'(\d{5}|\d{4}|\d{3})', url_data)[-1]
    print(url_data)
    count -= 1

# peak.html

# http://www.pythonchallenge.com/pc/def/linkedlist.php
