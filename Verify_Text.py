from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.maximize_window()

Text = driver.find_element(By.TAG_NAME, "h2").text
print(Text)


time.sleep(3)
Expected_text = "Test login"
assert Text == Expected_text, f" Text does not match! Expected: '{Expected_text}', but got: '{Text}'"

print(" Text matches expected value.")

driver.quit()
