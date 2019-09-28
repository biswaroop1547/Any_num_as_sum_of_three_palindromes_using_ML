import os
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

URL = 'http://www.rnta.eu/cgi-bin/three_palindromes/pal3.py'

driver = webdriver.Chrome()
num_list = []
for i in range(1, 100):

    driver.get(URL)
    writing_space = driver.find_element_by_id('number')
    writing_space.clear()
    writing_space.send_keys(i)
    writing_space.submit()
    nums = []
    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    for tag in soup.find_all('font'):

        if "is a palindrome" in tag.text:
            continue

        if "-" in tag.text:
            break

        nums.append(tag.text)
    num_list.append(nums)
for i in num_list:
    print(i)

print("the length is ", len(num_list))
