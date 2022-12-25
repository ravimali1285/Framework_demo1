from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest
driver = None
@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("-------------setup-----------")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    yield
    print("------teardown------")
    driver.quit()
def test_googletitle(init_driver):
    assert driver.title == "Google1"
def test_url(init_driver):
    assert driver.current_url == "https://www.google.com/"
