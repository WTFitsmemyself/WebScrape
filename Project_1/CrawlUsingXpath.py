from lxml import etree

src = "src/web_page.html"
tree = etree.parse(src)
print(tree)
tree_paragraph = tree.xpath("//title/text()")[0]
tree_hello = tree.xpath("//p/text()")[0]
string_tree = etree.tostring(tree)
li_list = tree.xpath("//li")

for li in li_list:
    lisT = ''.join(map(str.strip, li.xpath(".//text()")))
    print(lisT)
