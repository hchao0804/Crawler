import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'
}

# response = requests.get('http://httpbin.org/get', headers=headers)
# print(type(response))
# print(response.reason)
# print(response.status_code)
# print(type(response.text))
#
# print(response.json())
# print(type(response.json()))
# print(response.json()['url'])

# form = {"name": 'Han', 'age': '23'}
#
# image = {'file': open('image.png', 'rb')}
# r = requests.post("http://httpbin.org/post", files=image)
# print(r.text)


form = {"name": 'Han', 'age': '23'}
file = {'image': open('image.png', 'rb')}
respone_file = requests.post("http://httpbin.org/post", files=file)
print(respone_file.text)

respone_cookies = requests.get('https://www.baidu.com')
print(respone_cookies.cookies)
print(type(respone_cookies.cookies))
for key,value in respone_cookies.cookies.items():
    print(key + '=' + value)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)