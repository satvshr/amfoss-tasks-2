from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError

link = 'https://en.wikipedia.org/wiki/Malala_Yousafzai'
print(link)
res = requests.get(link) 
soup = BeautifulSoup(res.text, 'html.parser')

for link in soup.select('a'):  #extracting all the URLs found within a page’s <a> tags
    try:
        b = str(link.get('href'))
        if b == "None" or "#" in b:
            continue
        c = 'https://en.wikipedia.org' + b
        if '/wiki/' not in b:
            c = b
        if 'http' not in c:
            continue
        print(c)
        download = requests.get(c)
        download.raise_for_status()
        # print(download)
    except Exception:
        print('ERROR! The link you are trying to download is broken!')
