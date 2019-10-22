from bs4 import BeautifulSoup
import re

log = open('log.txt', 'r',encoding='utf-8')
out = open('out.txt', 'a',encoding='utf-8')
text = log.read()

# text = filter_tags(text)

soup = BeautifulSoup(text)

votes = soup.find_all("div", "apphub_CardContentMain")

for i in votes:
    # print(i.get_text())

    temp = i.get_text().replace('\t', '')
    temp = re.sub("\n+", "\n", temp)
    print(temp)
    out.write(temp)


    # print(' '.join(i.get_text().split()))
    # out.write(' '.join(i.get_text().split()))

    # print(re.sub(" +", " ", i.get_text()))
    # out.write(re.sub(" +", " ", i.get_text()))

    # temp = BeautifulSoup(i)
    # print(temp.div["found_helpful"])