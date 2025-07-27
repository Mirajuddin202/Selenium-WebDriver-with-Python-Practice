import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.get("https://demo.automationtesting.in/Register.html")
time.sleep(3)
elements =driver.find_element(By.ID,"checkbox1").get_attribute("value")
print(elements)
time.sleep(2)