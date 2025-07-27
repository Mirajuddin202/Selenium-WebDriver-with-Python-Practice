import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(3)
Alert_btn=driver.find_element(By.CSS_SELECTOR,"#content > div > ul > li:nth-child(3) > button")
Alert_btn.click()
time.sleep(3)
alert=driver.switch_to.alert
alert_text=alert.text
time.sleep(3)
alert.send_keys("This is Miraj")
alert.accept()
time.sleep(3)