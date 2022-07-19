from lxml import etree

src = "./src/web_page.html"
tree = etree.parse(src)
tree_paragraph = tree.xpath("//title/text()")[0]
tree_list = tree.findall("body/ul/li")
string_tree = etree.tostring(tree)

print(string_tree)
print(tree_paragraph)

for li in tree_list:
    a = li.find("a")
    if a is not None:
        print(f"{li.text.strip()} {a.text}")
    else:
        print(li.text)
