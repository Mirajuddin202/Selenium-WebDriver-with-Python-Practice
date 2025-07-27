from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://qa-automation-practice.netlify.app/radiobuttons")
print(driver.find_element(By.ID,"radio-button1").is_selected())
time.sleep(2)
driver.find_element(By.ID,"radio-button1").click()
time.sleep(2)
print(driver.find_element(By.ID,"radio-button1").is_selected())
time.sleep(2)
driver.find_element(By.ID,"radio-button2").click()
print(driver.find_element(By.ID,"radio-button2").is_selected())
time.sleep(2)
print(driver.find_element(By.ID,"radio-button1").is_selected())