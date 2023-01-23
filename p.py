from bs4 import BeautifulSoup
import requests, sys, pyperclip
if len(sys.argv) > 1:
    # Get address from command line.
    address = ' '.join(sys.argv[1:])

# TODO: Get address from clipboard.

else:
    # Get address from clipboard.
    address = pyperclip.paste()

link = 'https://imgur.com/search?q=' + address
print(link)
res = requests.get(link) 
soup = BeautifulSoup(res.text, 'html.parser')

for link in soup.select('a'):  #extracting all the URLs found within a page’s <a> tags
    b = link.get('href')
    if '/gallery' in str(b):
        c = b.replace('/gallery/', '')
        a = "https://i.imgur.com/" + c + ".png"
        download = requests.get(a)
        download_place = '/home/satvshr/Desktop/pics/' + c + '.png'
        print(download_place)
        with open(download_place, 'wb') as f:
            f.write(download.content)

