from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
chrome_options = Options()
chrome_options.add_argument('--headless') #添加Chrome Headless
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.baidu.com")
print(browser.current_url)

soup = BeautifulSoup("<p>Hello</p>","lxml")
print(soup.p.string)

with open("C:/Users/v-chah/Desktop/results.txt") as f:
     print(f.read())