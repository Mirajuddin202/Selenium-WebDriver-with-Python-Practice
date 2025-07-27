import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://demoqa.com/buttons")
driver.maximize_window()
actions=ActionChains(driver)
right_click_button=driver.find_element(By.ID,"rightClickBtn")
driver.execute_script("arguments[0].scrollIntoView()",right_click_button)
actions.context_click(right_click_button).perform()
time.sleep(4)
