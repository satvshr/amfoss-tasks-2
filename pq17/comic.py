from bs4 import BeautifulSoup
import requests, time
z = True
num = 2732
while z:
    try:
        link = 'https://xkcd.com/' + str(num) + '/'
        a = []
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        #link = soup.select('#comic')
        link = soup.find_all("img")
        for i in link:
            a.append(i.get('alt'))
        #print(a)
        src = a[2]
        print(type(src))

        x = src.replace(' ', '_')
        x = x.lower()
        link = 'https://imgs.xkcd.com/comics/' + x +'.png'
        download = requests.get(link)
        place = '/home/satvshr/Desktop/comics/' + x + '.png'
        print(link)
        with open(place, 'wb') as f:
            f.write(download.content)
        num += 1
    except requests.exceptions.HTTPError:
        print('No comic was found. Will try again in 2 days.')

    for i in range(172800):
        time.sleep(1)

