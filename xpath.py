from lxml import etree


# text = '''
# <div>
#     <ul>
#          <li class="item-0"><a href="link1.html">first item</a></li>
#          <li class="item-1"><a href="link2.html">second item</a></li>
#          <li class="item-inactive"><a href="link3.html">third item</a></li>
#          <li class="item-1"><a href="link4.html">fourth item</a></li>
#          <li class="item-0"><a href="link5.html">fifth item</a>
#      </ul>
#  </div>
# '''
# html = etree.HTML(text)
# result = etree.tostring(html)
# print(result.decode('utf-8'))

# html = etree.parse('./test.html', etree.HTMLParser())
# result = etree.tostring(html)
# result = html.xpath('//li')
# print(result)

# //用来从当前--获得子孙节点，/用来直接获得子节点
# html = etree.parse('test.html', etree.HTMLParser())
# result = html.xpath('//li/a')
# print(result)

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//a[@href="link4.html"]/../@class')
# result = html.xpath('//a[@href="link4.html"]/parent::*/@class')
# print(result)

# html = etree.parse('./test.html', etree.HTMLParser())
# result = html.xpath('//li[@class="item-0"]/text()')
# print(result)

html = etree.parse('./test.html', etree.HTMLParser())
result = html.xpath('//li[@class="item-0"]//text()')
print(result)

html2 = etree.parse('./test.html', etree.HTMLParser())
result2 = html.xpath('//li[@class="item-0"]/a/text()')
print(result2)