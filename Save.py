import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
import json
import csv
import pandas

'''TXT

url = 'https://www.zhihu.com/explore'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
    }

html = pq(url=url, headers=headers)
items = html('.explore-tab .feed-item').items()

for item in items:
    title = item.find('h2').text()
    author = item.find('.author-link-line').text()
    answer = pq(item.find('.content').html()).text()
    with open('explore.txt', 'a', encoding='utf-8') as f:
        f.write('\n'.join([title, author, answer]))
        f.write('\n' + '='*40 + '\n')
'''


"""
#JSON

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
'''

with open('data.json', 'w') as file:
    data = json.loads(str)
    file.write(json.dumps(data, indent = 2))
    
"""

# csv

with open('data.csv', 'w', newline='') as file:
    # data = csv.writer(file, delimiter=' ')
    # data.writerow(['id','name','age'])
    # data.writerows([['id','name','age'], ['10001', 'a', 312], ['10002', 'b', 313], ['10003', 'c', 314]])
    # data.writerow(['10002', 'b', 13])
    # data.writerow(['10003', 'c', 14])
    fieldnames=["name", 'number', "address"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "a", "number": "123", "address": "aaa"})
    writer.writerow({"name": "b", "number": "1233", "address": "bbb"})
    writer.writerow({"name": "c", "number": "1234", "address": "ccc"})


with open('data.csv', 'r') as read:
    reader = csv.reader(read)
    for row in reader:
        print(row)

df = pandas.read_csv('data.csv')
print(df)