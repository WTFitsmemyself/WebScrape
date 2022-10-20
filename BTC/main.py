import requests
import pandas as pd
from bs4 import BeautifulSoup as Bs

first_page = 1
last_page = 2573157538607026564968244111304175730063056983979442319613448069811514699875
base_url = "https://privatekeys.pw/keys/bitcoin/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

for page_num in range(first_page, last_page):
    final_url = base_url + str(page_num)
    responce = requests.get(final_url, headers=headers)
    soup = Bs(responce.content, "html.parser")
    pretty = soup.prettify()
    print(pretty)

