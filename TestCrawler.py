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

form = {"name": 'Han', 'age': '23'}

image = {'file': open('image.png', 'rb')}
r = requests.post("http://httpbin.org/post", files=image)
print(r.text)

