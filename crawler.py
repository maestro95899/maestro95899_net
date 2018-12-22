WIKI_PAGE_DEPTHS = {}

print(len(WIKI_PAGE_DEPTHS))

import requests
from bs4 import BeautifulSoup
import sys

dict = {}
pages = set()

proxies = {
    'http': 'http://5.135.164.72:3128',
}


def walk(adress, wiki_lang, deepth, proxy=False):
    global pages
    global dict
    print(adress)
    try:
        if proxy:
            print('try req with proxi')
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
                            #print('https://' + wiki_lang + '.wikipedia.org' + tag.get('href'))
                            yield 'https://' + wiki_lang + '.wikipedia.org' + tag.get('href')
                            #walk(base + tag.get('href'), deepth + 1)
            #print('end')
        else:
            return False
    except requests.exceptions.SSLError:
        print('SSLError')
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
        print('----------------------------------------')
        print(dict)

def is_not_accessed(adress):
    flag = False
    try:
        rsp = requests.get(adress)
        #flag = True
    except BaseException:
        print('Use proxy')
        flag = True
    return flag

def run():
    wiki_lang = 'rmy'
    adress = 'https://rmy.wikipedia.org/wiki/Sherutni_patrin'
    max_deepth=1

    if len(sys.argv) > 1:
        adress = sys.argv[1]
        if len(sys.argv) > 2:
            wiki_lang = sys.argv[2]
            if len(sys.argv) > 3:
                max_deepth = int(sys.argv[3])
                if len(sys.argv) > 4:
                    adr = 'http://' + sys.argv[4]
                    global proxies
                    proxies = {
                        'http': adr,
                    }

    bfs(adress, wiki_lang, is_not_accessed(adress), max_deepth=max_deepth)

run()
