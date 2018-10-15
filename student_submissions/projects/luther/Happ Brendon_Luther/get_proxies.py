import requests
from lxml.html import fromstring

def get_proxies():
    url = 'https://free-proxy-list.net/'
    page = requests.get(url)
    parser = fromstring(page.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:50]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            #Grabbing IP and corresponding PORT
            proxy = ":".join(['http', '//'+i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies


proxies = list(get_proxies())

with open('proxies.txt', 'w') as output:
    for item in proxies:
        output.write("%s\n" % item)