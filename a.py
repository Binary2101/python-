import requests
from http.cookies import SimpleCookie
from bs4 import BeautifulSoup
import re

out = open('out.txt', 'a',encoding='utf-8')
log = open('log.txt', 'a',encoding='utf-8')

# raw_cookie = ""
# cookie = SimpleCookie(raw_cookie)
# requests_cookies = dict([(c, cookie[c].value) for c in cookie])
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
        }

# offset+=10， page+=1
url = "https://steamcommunity.com/app/998940/homecontent/?userreviewsoffset={offset}&p={page}&workshopitemspage={page}&readytouseitemspage={page}&mtxitemspage={page}&itemspage={page}&screenshotspage={page}&videospage={page}&artpage={page}&allguidepage={page}&webguidepage={page}&integratedguidepage={page}&discussionspage={page}&numperpage=10&browsefilter=mostrecent&browsefilter=mostrecent&appid=322330&appHubSubSection=10&appHubSubSection=10&l=schinese&filterLanguage=english&searchText=&forceanon=1"

for i in range(1, 21):
    # print(url.format(offset=(i-1)*10, page=i))
    a = requests.get(url.format(offset=(i-1)*10, page=i))
    a.encoding = 'utf-8'
    log.write(a.text)
    soup = BeautifulSoup(a.text)
    votes = soup.find_all("div", "apphub_CardTexZtContent")
    for i in votes:
        # print(i.get_text())
        temp = i.get_text().replace('\t', '')
        temp = re.sub("\n+", "\n", temp)
        temp = str.lower(temp)
        temp = re.sub("[^A-Za-z\n]", " ", temp)
        print(temp)
        out.write(temp)


# a = requests.get(url.format(offset=(1-1)*10, page=1))
# a.encoding = 'utf-8'
# log.write(a.text)
