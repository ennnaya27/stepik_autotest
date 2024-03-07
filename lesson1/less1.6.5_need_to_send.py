from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link='http://suninjuly.github.io/registration2.html'

try:
    browser=webdriver.Chrome()
    browser.get(link)
    input1=browser.find_element(By.CSS_SELECTOR, '.first_block .first')
    input1.send_keys("Галина")
    input2 = browser.find_element(By.CSS_SELECTOR, '.first_block .second')
    input2.send_keys("Зинченко")
    input3=browser.find_element(By.CSS_SELECTOR, '.first_block .third')
    input3.send_keys("GalyaZ@mail.ru")
    button=browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()
    time.sleep(3)
    text_elt=browser.find_element(By.CSS_SELECTOR, 'h1')
    text=text_elt.text
    assert 'Congratulations! You have successfully registered!'==text
finally:
    time.sleep(5)
    browser.quit()