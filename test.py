import os
from bs4 import BeautifulSoup
import urllib
import urllib.parse
import urllib.request
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv

URL = 'http://www.rnta.eu/cgi-bin/three_palindromes/pal3.py'

driver = webdriver.Chrome()
dataset = []
for i in range(1000, 4000):

    driver.get(URL)
    writing_space = driver.find_element_by_id('number')
    writing_space.clear()
    writing_space.send_keys(i)
    writing_space.submit()
    nums = {"Number": i, "First": 0, "Second": 0, "Third": 0}
    html = driver.page_source
    soup = BeautifulSoup(html, features="html.parser")
    count = 0
    for tag in soup.find_all('font'):

        if "is a palindrome" in tag.text:
            nums["First"] = i
            break

        if "-" in tag.text:
            break

        if count == 0:
            nums["First"] = tag.text

        elif count == 1:
            nums["Second"] = tag.text

        elif count == 2:
            nums["Third"] = tag.text

        count += 1
    dataset.append(nums)


# print(dataset)

with open("data.csv", "a") as csvFile:
    fields = ["Number", "First", "Second", "Third"]
    writer = csv.DictWriter(csvFile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(dataset)

driver.close()
csvFile.close()
