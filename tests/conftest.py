import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from config import Config

@pytest.fixture(scope="class")
def setup(request):
    options = Options()
    if Config.HEADLESS:
        options.add_argument("--headless=new")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.maximize_window()
    driver.get(Config.BASE_URL)
    request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture
def test_photo_jpg():
    """Fixture providing path to test JPG photo"""
    return os.path.join(os.path.dirname(__file__), "test_data", "test_photo.jpg")