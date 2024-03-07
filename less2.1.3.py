from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
  browser = webdriver.Chrome()
  browser.get("https://suninjuly.github.io/math.html")
  x_elem = browser.find_element(By.CSS_SELECTOR, "#input_value")

  x = x_elem.text
  y = calc(x)
  browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

  browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()

  browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()

  browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(15)
    browser.quit()