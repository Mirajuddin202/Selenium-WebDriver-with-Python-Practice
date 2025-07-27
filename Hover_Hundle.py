import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/jqueryui/menu#")
time.sleep(3)
hover=driver.find_element(By.CSS_SELECTOR,"#ui-id-3 > a")
action=ActionChains(driver)
action.move_to_element(hover)
action.perform()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#ui-id-8 > a").click()
time.sleep(3)