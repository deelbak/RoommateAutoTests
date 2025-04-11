from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "Login")

    def load(self, base_url):
        self.driver.get(f"{base_url}/login")

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()