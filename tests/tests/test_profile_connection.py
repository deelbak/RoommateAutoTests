import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:3000/profile/2"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_user_connection_and_match_score(driver):
    driver.get(BASE_URL)

    connection_status = driver.find_element(By.XPATH, "//*[contains(text(), 'Connected')]")
    assert connection_status.is_displayed()

    score_element = driver.find_element(By.XPATH, "//div[contains(@class, 'Match') or contains(text(), 'Match Score')]/preceding-sibling::div")
    score = int(score_element.text.strip())
    assert score > 50
