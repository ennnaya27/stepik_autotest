from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://suninjuly.github.io/find_xpath_form"

with webdriver.Chrome() as browser:
    browser.get(url)
    browser.find_element(By.NAME, "first_name").send_keys("Galina")
    browser.find_element(By.NAME, "last_name").send_keys("Zinchenko")
    browser.find_element(By.NAME, "firstname").send_keys("Samara")
    browser.find_element(By.ID, "country").send_keys("Russia")
    for elem in browser.find_elements(By.CLASS_NAME, "btn"):
        if elem.text == "Submit":
            elem.click()
            alert_box = browser.switch_to.alert
            print(alert_box.text)
            alert_box.accept()
            break