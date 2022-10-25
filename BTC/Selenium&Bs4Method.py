# Library importing
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# Page specification
first_page = 1
last_page = 2573157538607026564968244111304175730063056983979442319613448069811514699875

# Headless selenium driver
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# URL for scrape
base_url = "https://privatekeys.pw/keys/bitcoin/"

# Loop of the program
for page_num in range(2114, last_page):
    final_url = base_url + str(page_num)
    driver.get(final_url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    result = soup.find("span", {"class": "badge bg-light text-dark"})
    text_final = result.text
    if float(text_final) > 0:
        print(f"{page_num}: {text_final}")
    else:
        print(f"{page_num}: NONE")
