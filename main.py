from lxml import etree

src = "./src/web_page.html"
tree = etree.parse(src)
tree_paragraph = tree.xpath("//title/text()")[0]
tree_hello = tree.xpath("//p/text()")[0]
string_tree = etree.tostring(tree)

print(string_tree)
print(tree_hello)
print(tree_paragraph)

for i in range(0, 2):
    tree_list = tree.xpath("//li/text()")[i]
    print(tree_list)
