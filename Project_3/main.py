import requests
from bs4 import BeautifulSoup as Bs

src = 'https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
responce = requests.get(src)
soup = Bs(responce.content, "html.parser")
print(responce.text)
