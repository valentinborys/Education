import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.mark.parametrize('creds', [('valentyn1@test.com', 'test'),
                                   ('valentyn2@test.com', 'test'),
                                   ('valentyn3@test.com', 'test')
                                   ])
def test_login(creds):
    login, password = creds
    driver = webdriver.Chrome()
    driver.get("https://magento.softwaretestingboard.com/customer/account/login")
    driver.maximize_window()

    driver.find_element(By.ID, "email").send_keys(login)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "send2").click()

    error_message = driver.find_element(By.CSS_SELECTOR, "[data-ui-id = 'message-error']").text

    assert error_message == ('The account sign-in was incorrect or your account is disabled temporarily. '
                             'Please wait and try again later.')

    time.sleep(1)
