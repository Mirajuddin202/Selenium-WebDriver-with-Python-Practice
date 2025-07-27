import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/select-menu.php")
driver.maximize_window()
time.sleep(3)
dropdown=driver.find_element(By.XPATH,"//span[contains(@class,'mbsc-textfield mbsc-textfield-outline mbsc-select mbsc-textfield-stacked mbsc-textfield-outline-stacked mbsc-textarea')]")
dropdown.click()
time.sleep(3)
driver.find_element(By.XPATH,"//div[normalize-space()='Books']").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[43]").click()
time.sleep(4)
