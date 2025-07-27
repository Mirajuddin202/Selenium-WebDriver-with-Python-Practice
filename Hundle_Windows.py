import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)
driver.switch_to.new_window()
time.sleep(3)
driver.get("https://the-internet.herokuapp.com/")
Total_Tabs=len(driver.window_handles)
print(Total_Tabs)
value=driver.window_handles
print(value)
current_Tab=driver.current_window_handle
print(current_Tab)
time.sleep(3)
First_Tab=driver.window_handles[0]
driver.switch_to.window(First_Tab)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.orangehrm-login-forgot > p").click()
time.sleep(3)
