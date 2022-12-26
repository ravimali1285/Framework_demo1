from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(params=["chrome", "firefox"],scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Chrome will launch")
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("Firefox will launch")
    request.cls.driver = web_driver
    yield
    web_driver.close()