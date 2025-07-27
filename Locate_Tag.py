from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()
time.sleep(3)

username=driver.find_element(By.TAG_NAME,"input")
username.send_keys("student")
password=driver.find_element(By.ID,"password")
password.send_keys("Password123")
submit=driver.find_element(By.CLASS_NAME,"btn")
submit.click()
