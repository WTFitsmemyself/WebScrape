from lxml import etree

src = "./src/web_page.html"
tree = etree.parse(src)
html = tree.getroot()
tree_paragraph = html.cssselect("title")[0]

print(tree_paragraph.text)

# li_list = tree.xpath("//li")
# for li in li_list:
#     lisT = ''.join(map(str.strip, li.xpath(".//text()")))
#     print(lisT)
