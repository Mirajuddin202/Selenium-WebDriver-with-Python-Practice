from selenium.webdriver.common.by import By
import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
username_enter="student"
Password_Enter="Password123"
username=driver.find_element(By.ID,"username")
username.send_keys(username_enter)
Password=driver.find_element(By.ID,"password")
Password.send_keys(Password_Enter)
Submit=driver.find_element(By.ID,"submit")
Submit.click()
Logout=driver.find_element(By.LINK_TEXT,"Log out")
Logout_text=Logout.text
Expected_text="Log out"
assert Logout_text==Expected_text