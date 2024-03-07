from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/simple_form_find_task.html"

with webdriver.Chrome() as browser:
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Galya")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Zinchenko")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Samara")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(30)