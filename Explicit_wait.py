from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://bstackdemo.com/")

# Click "Add to cart"
driver.find_element(By.XPATH, "//div[@id='3']//div[@class='shelf-item__buy-btn'][normalize-space()='Add to cart']").click()

# Wait for the "Checkout" button to appear and then click it
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[@class='buy-btn']"))
)

element.click()

time.sleep(5)
driver.quit()
