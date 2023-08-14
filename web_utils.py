# importing webdriver from selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import re, html, os, urllib, shutil, bs4, csv, time, glob, pynput
import file_utils, graph_utils

def get_page (url):
    options = Options()
    options.add_argument('--headless')
    options.add_argument("--window-size=1920,1080")
    options.add_argument('--disable-gpu')
    service = Service(ChromeDriverManager(version='114.0.5735.90').install())
    driver = webdriver.Chrome (service=service, options=options)
    driver.set_page_load_timeout(15)
    driver.get(url)
    WebDriverWait(driver, 100).until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    source = driver.page_source
    
    driver.close()

    soup = bs4.BeautifulSoup(source, 'html.parser')
    return str(soup.prettify())

def grab_urls (source):
    urls = []
    regex = "(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+"
    matches = re.findall(regex, source)

    for match in matches:
        if "http" in match[:4]: urls.append(match)
        elif "//" in match[:2]:
            match = "http:" + match
            urls.append(match)

    return list(set(urls))
