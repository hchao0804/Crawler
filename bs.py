from bs4 import BeautifulSoup
'''
html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup=BeautifulSoup(html, 'lxml')
soup.prettify()
# print(soup.title.string) # string 和 text返回的类型是不一样的
# print(soup.p.string)
# print(soup.p.string)
# print(soup.p.attrs)
# print(soup.p['class'])
# print(soup.head.title)  # 返回 Tag 类型
# print(type(soup.head.title))
# print(soup.body.p.contents)  # 返回直接节点组成的列表

# print(list(soup.p.children))
# for i, child in enumerate(soup.p.children):
#      print(i, child)

# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)


for i in range(3):
    print(list(enumerate(soup.p.parents))[i])
'''


html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
#soup=BeautifulSoup(html, 'lxml')
# print(soup.find_all(name='ul'))
'''
for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
print('\n')
print((soup.find_all(name='ul')[0]).find_all(name='li'))

print(soup.find_all(attrs={'class':'list','id':'list-1'}))
'''

html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
soup=BeautifulSoup(html, 'lxml')
# for li in soup.select('li'):
#     print('Get Text:', li.get_text())
#     print('Get Text:', type(li.get_text()))
#     print('String:', li.string)
#     print('String:', type(li.string))
print(soup.select('ul li'))

print(soup.select('ul'))
for ul in soup.select('ul'):
    print(ul.select('li'))