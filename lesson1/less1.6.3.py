from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")

    value = list(range(1,101))

    for number, element in enumerate(elements):
        element.send_keys(f"{value[number]}")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:

    time.sleep(30)

    browser.quit()
