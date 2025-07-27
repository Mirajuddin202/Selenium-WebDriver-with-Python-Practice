from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page")
time.sleep(3)
element=driver.find_element(By.TAG_NAME,'h2')
element.screenshot("C:\\Users\\HP\\PycharmProjects\\PythonProject\\Screenshot.\\test.png")
driver.get_screenshot_as_file("C:\\Users\\HP\\PycharmProjects\\PythonProject\\Screenshot.\\test1.png")

time.sleep(3)