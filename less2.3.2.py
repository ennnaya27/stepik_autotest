from selenium import webdriver

from selenium.webdriver.common.by import By

import math

import time

 

def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))

 

with webdriver.Chrome() as browser:

  browser.get('https://suninjuly.github.io/redirect_accept.html')

  browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

  new_window = browser.window_handles[1]

  browser.switch_to.window(new_window)

  x_elem = browser.find_element(By.ID, "input_value")

  x = x_elem.text

  y = calc(x)

  browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

  browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

  time.sleep(10)