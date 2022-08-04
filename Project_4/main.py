import requests
from lxml import etree, html
from bs4 import BeautifulSoup as Bs

src = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
resp = requests.get(src)
soup = Bs(resp.text, "html.parser")
htmlP = soup.prettify()

tree = html.fromstring(htmlP)
print(tree.text)
