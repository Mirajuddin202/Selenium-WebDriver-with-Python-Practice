from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time



driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/drag_and_drop")
time.sleep(3)
source=driver.find_element(By.ID,"column-a")
destination=driver.find_element(By.ID,"column-b")
action =ActionChains(driver)
action.drag_and_drop(source,destination).perform()
time.sleep(3)