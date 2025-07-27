from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/v1/index.html")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@id='login-button']").click()
driver.find_element(By.XPATH,"//button[normalize-space()='Open Menu']").click()
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Logout").click()
time.sleep(10)