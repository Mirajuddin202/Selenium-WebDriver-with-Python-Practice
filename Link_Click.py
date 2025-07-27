from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://demo.guru99.com/")
driver.maximize_window()
time.sleep(2)
Link=driver.find_element(By.PARTIAL_LINK_TEXT,"Bank")
Link.click()
time.sleep(3)