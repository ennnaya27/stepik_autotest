import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math

try:
    link = 'https://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)
    result = sum([int(_.text) for _ in browser.find_elements(By.CSS_SELECTOR, '[id^=num]')])
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(result))
    browser.find_element(By.TAG_NAME, 'button').click()
    time.sleep(30)
finally:
    browser.quit()
