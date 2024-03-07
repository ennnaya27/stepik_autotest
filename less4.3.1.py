from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.common.exceptions import NoAlertPresentException # в начале файла

browser = webdriver.Chrome()
browser.get('http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear')

browser.find_element(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket').click()
time.sleep(1)


alert = browser.switch_to.alert
x = alert.text.split(" ")[2]
answer = str(math.log(abs((12 * math.sin(float(x))))))
time.sleep(1)
alert.send_keys(answer)
alert.accept()


print(browser.switch_to.alert.text.split()[-1])
time.sleep(30)
browser.quit()