from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
time.sleep(3)

checkbox=driver.find_element(By.ID,"hobbies")
if not checkbox.is_selected():
    checkbox.click()
    time.sleep(5)