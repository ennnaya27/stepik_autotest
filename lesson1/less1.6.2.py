import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'http://suninjuly.github.io/find_link_text'
driver = webdriver.Chrome()
link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

try:
    driver.get(url)
    link = driver.find_element(By.LINK_TEXT, link_text)
    link.click()

    first_name = driver.find_element(By.TAG_NAME, "input")
    first_name.send_keys('Galya')
    
    last_name = driver.find_element(By.NAME, "last_name")
    last_name.send_keys("Zinchenko")
    
    city = driver.find_element(By.CLASS_NAME, "city")
    city.send_keys("Samara")
    
    country = driver.find_element(By.ID, "country")
    country.send_keys("Russia")
    
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()
finally:
    time.sleep(3)
    driver.quit()
