from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import tesserocr  # 安装完tesseract后，添加TESSDATA_PREFIX环境变量
from PIL import Image

chrome_options = Options()
chrome_options.add_argument('--headless')  # 添加Chrome Headless
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.baidu.com")
print(browser.current_url)

soup = BeautifulSoup("<p>Hello</p>", "lxml")
print(soup.p.string)

print(tesserocr.tesseract_version())
print(tesserocr.get_languages())
image = Image.open("Untitled.png")  # 下载新的tessdata package 代替自带的tessdata
print(tesserocr.image_to_text(image))
