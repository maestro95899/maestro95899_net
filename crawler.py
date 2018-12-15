WIKI_PAGE_DEPTHS = {}

print(len(WIKI_PAGE_DEPTHS))

import requests
from bs4 import BeautifulSoup
import sys

dict = {}
pages = set()

proxies = {
    'http': 'http://5.61.199.55:54767',
    'https': 'https://1.2.169.9:55009',
}


def walk(adress, wiki_lang, deepth, proxy=False):
    global pages
    global dict
    print(adress)
    try:
        if proxy:
            req = requests.get(adress, proxies=proxies)
        else:
            req = requests.get(adress)
        if req.status_code == 200:
            soup = BeautifulSoup(req.text, "lxml")

            adress_name = soup.findAll('a', attrs={"dir": "ltr"})[0].text
            if adress_name.find(wiki_lang + '.wikipedia.org') > -1:
                begin = adress_name.find('title=')
                if begin > -1:
                    if adress_name.find('&') != -1:
                        name = adress_name[begin + 6:adress_name.find('&')]
                    else:
                        name = adress_name[begin + 6:]
                    if name.find(':') == -1:
                        deep = dict.setdefault(name, deepth)
                        if deepth < deep:
                            dict[name] = deepth
            #print(deepth)
            tags = soup.body.find_all('a')
            #print('here')
            for tag in tags:
                #print(tag)
                if tag.get('href'):
                    if (tag.get('href').find('/wiki/') > -1) and\
                            (tag.get('href').find('https://') == -1) and \
                            (tag.get('href').find('.png') == -1) and \
                            (tag.get('href').find('.jpg') == -1) and \
                            (tag.get('href').find(':') == -1) and \
                            (tag.get('href').find('#') == -1) and \
                            (tag.get('href').find('?') == -1) and \
                            (tag.get('href').find('=') == -1) and \
                            (tag.get('href').find('&') == -1) and \
                            (tag.get('href').find('.gif') == -1) and \
                            (tag.get('href').find('.svg') == -1) and \
                            (tag.get('href').find('//') == -1):
                        if tag.get('href') not in pages:
                            pages.add(tag.get('href'))
                            print('https://' + wiki_lang + '.wikipedia.org' + tag.get('href'))
                            yield 'https://' + wiki_lang + '.wikipedia.org' + tag.get('href')
                            #walk(base + tag.get('href'), deepth + 1)
            #print('end')
        else:
            return False
    except BaseException:
        print('fail')
    return False




def bfs(adress, wiki_lang, proxy, max_deepth=None):
    level = [adress]
    new_level = []
    deepth = 0
    while (len(level) > 0) and ((max_deepth is not None) and (max_deepth >= deepth)):
        for page in level:
            res = list(walk(page, wiki_lang, deepth, proxy))
            if res:
                new_level.extend(res)
        deepth += 1
        level = new_level.copy()
        new_level = []
        print('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(dict)

def is_not_accessed(adress):
    flag = False
    try:
        rsp = requests.get(adress)
    except BaseException:
        print('Use proxy')
        flag = True
    return flag

def run():
    wiki_lang = 'rmy'
    adress = 'https://rmy.wikipedia.org/wiki/Sherutni_patrin'
    base = 'https://rmy.wikipedia.org'
    max_deepth=0

    if sys.argv:
        adress = sys.argv[1]
        if len(sys.argv) > 2:
            wiki_lang = sys.argv[2]
            if len(sys.argv) > 3:
                max_deepth = int(sys.argv[3])

    base = 'https://' + wiki_lang + '.wikipedia.org'

    bfs(adress, wiki_lang, is_not_accessed(adress), max_deepth=max_deepth)



run()
"""
#walk('https://rmy.wikipedia.org/wiki/Kale', 0)
bloced_adress = 'https://rutracker.org/forum/index.php'
wiki_lang = 'rmy'
adress = 'https://rmy.wikipedia.org/wiki/Sherutni_patrin'
for param in sys.argv:
    print(param)
bfs(adress, wiki_lang, is_not_accessed(adress), max_deepth=1)
print(dict)
"""

# rsp = requests.get('https://rmy.wikipedia.org/wiki/Sherutni_patrin')
# print(rsp.status_code)
# rsp = requests.get('https://rmy.wikipedia.org/wiki/Kale')
# print(rsp.status_code)
# soup = BeautifulSoup(rsp.text, "lxml")
# print(soup.body.prettify())
# tags = soup.body.find_all('a')
# for tag in tags:
#    print(tag.get('href'))
# req = requests.get(base + '/wiki/Franchiya')
# print(req.status_code)

"""
rsp = requests.get('https://rmy.wikipedia.org/wiki/Sherutni_patrin')
print(rsp.status_code)

soup = BeautifulSoup(rsp.text, "lxml")
#print(soup.prettify())
tags = soup.find_all('a')
#for tag in tags:
#    print(tag.get('href'))

adress_name = soup.findAll('a', attrs={"dir": "ltr"})[0].text
if adress_name.find('rmy.wikipedia.org') > -1:
    begin = adress_name.find('title=')
    name = adress_name[begin + 6:adress.find('&')]
    print(name)
print(soup.findAll('a', attrs={"dir": "ltr"})[0].text)

"""
