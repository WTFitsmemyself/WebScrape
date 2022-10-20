import requests
from lxml import html

src = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
resp = requests.get(src)

tree = html.fromstring(resp.text)
title = tree.xpath("//*[@id='content_inner']/article/div[1]/div[2]/h1/text()")[0]
price = tree.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[1]/text()')[0]
stock_left = tree.xpath('//*[@id="content_inner"]/article/div[1]/div[2]/p[2]/text()')[1]
description = tree.xpath('//*[@id="content_inner"]/article/p/text()')[0]

print(title)
print(price)
print(stock_left)
print(description)
