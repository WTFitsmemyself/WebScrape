import requests
from lxml import html

private_keys = []
address_comp = []
address_un_comp = []

first_page = 1
last_page = 2573157538607026564968244111304175730063056983979442319613448069811514699875
base_url = "https://privatekeys.pw/keys/bitcoin/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}

for page_num in range(first_page, 100+1):
    final_url = base_url + str(page_num)
    resp = requests.get(final_url, headers=headers)
    tree = html.fromstring(resp.text)
    key = tree.xpath('//*[@class="text-nowrap"]/a/text()')
    address_c = tree.xpath('//*[@class="text-nowrap"][2]')
    address_u_c = tree.xpath('//*[@class="text-nowrap"][3]')

    private_keys.append(key)

    for add in address_c:
        address_ok = ''.join(map(str.strip, add.xpath(".//text()")))
        address_comp.append(address_ok)

    for add in address_u_c:
        address_ok = ''.join(map(str.strip, add.xpath(".//text()")))
        address_un_comp.append(address_ok)


for page_num in range(first_page, 100+1):
    print(private_keys[page_num][0])
    print(address_comp[page_num])
    print(address_un_comp[page_num])
