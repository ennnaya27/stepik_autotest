from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
import pytest
import os

email = os.environ.get('MY_EMAIL')
password = os.environ.get('MY_PASSWORD')


@pytest.fixture
def browser():
    with webdriver.Chrome() as browser:
        yield browser


@pytest.mark.parametrize("url", ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                 "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"])
class Test_stepik:
    def test_guest_should_see_login_links(self, browser, url):
        text = ''
        browser.get(url)
        browser.implicitly_wait(8)
        browser.find_element(By.CLASS_NAME, 'st-link_style_button').click()
        browser.implicitly_wait(8)
        browser.find_element(By.ID, 'id_login_email').send_keys(email)  # здесь вводится e-mail
        browser.find_element(By.ID, 'id_login_password').send_keys(password)  # здесь вводится пароль
        browser.find_element(By.CLASS_NAME, 'sign-form__btn').click()
        time.sleep(9)
        answer = math.log(int(time.time()))
        browser.find_element(By.TAG_NAME, "textarea").send_keys(answer)
        browser.implicitly_wait(4)
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(1)
        feedback = WebDriverWait(browser, 10).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".smart-hints__hint"), "Correct!")
        )
        feedback_text = browser.find_element(By.CSS_SELECTOR, ".smart-hints__hint").text
        try:
            assert feedback_text == "Correct!"
        except AssertionError:
            text += feedback_text

if __name__ == "__main__":
    pytest.main()
