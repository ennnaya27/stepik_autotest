from pathlib import Path

from selenium import webdriver

from selenium.webdriver.common.by import By

import time

file_search = str(Path('test.txt').absolute())

with open('test.txt', 'w') as new_file:

    pass


 

with webdriver.Chrome() as browser:

    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, 'firstname').send_keys('Galina')

    browser.find_element(By.NAME, 'lastname').send_keys('Zinchenko')

    browser.find_element(By.NAME, 'email').send_keys('Galina@ya.ru')

    browser.find_element(By.NAME, 'file').send_keys(file_search)

    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()

    time.sleep(10)