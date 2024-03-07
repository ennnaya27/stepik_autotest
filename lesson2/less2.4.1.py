from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver

import math

import time

 

def calc(x):

  return str(math.log(abs(12*math.sin(int(x)))))

 

with webdriver.Chrome() as browser:

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))

    button = browser.find_element(By.ID, 'book').click()

    x_elem = browser.find_element(By.ID, "input_value")

    x = x_elem.text

    y = calc(x)

    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)

    browser.find_element(By.ID, 'solve').click()

    time.sleep(10)