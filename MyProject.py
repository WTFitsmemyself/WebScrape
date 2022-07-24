import requests
from lxml import etree

src = "https://www.hongkiat.com/blog/web-scraping-tools/"
data = requests.get(src)
html = data.content.decode("utf-8")
tree_para = etree
print(tree)
# print(html)

