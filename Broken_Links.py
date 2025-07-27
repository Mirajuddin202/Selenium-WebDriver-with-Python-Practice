import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
time.sleep(2)


links = driver.find_elements(By.TAG_NAME, "a")
total_links = len(links)
print(f"Total links: {total_links}")


for link in links:
    href = link.get_attribute('href')
    if href is None or not href.startswith("http"):
        continue
    try:
        response = requests.get(href)
        if response.status_code >= 400:
            print(f" Broken Link: {href} (Status code: {response.status_code})")
        else:
            print(f" Working Link: {href} (Status code: {response.status_code})")
    except Exception as e:
        print(f" Error checking link: {href} — {e}")


driver.quit()
