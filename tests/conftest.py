import pytest
from selenium import webdriver

from utilitues.Read_Properties import ReadProperties

driver=None


@pytest.fixture()
def setup(request):
    global driver
    driver = webdriver.Chrome()
    driver.get("https://www.asianpaints.com/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
