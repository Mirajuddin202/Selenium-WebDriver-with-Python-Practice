from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
time.sleep(3)
dropdown_element=driver.find_element(By.ID,"dropdown")
select= Select(dropdown_element)
select.select_by_index(1)
time.sleep(5)