import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.mark.usefixtures("init_driver")
class Basetest:
    pass
class Test_Hubspotlogin(Basetest):
    @pytest.mark.parametrize(
        "username, password",
        [
        ("admin1@gmail.com", "admin123"),
        ("admin23@gmail.com", "admin@1234"),
        ]
    )
    def test_maillogin(self,username,password):
        """
        This method is used to login in Hubspot.com
        :param username:
        :param password:
        :return:
        """
        self.driver.get("https://app.hubspot.com/login")
        self.driver.find_elements(By.XPATH,"//input[@id='username']").send_keys(username)
        time.sleep(3)
        self.driver.find_elements(By.ID, "password").send_keys(password)
        time.sleep(2)
