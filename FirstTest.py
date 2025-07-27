from selenium.webdriver.common.by import By
import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://practicetestautomation.com/practice-test-login/")
print("Open Browser")
title=browser.title
print(title)
