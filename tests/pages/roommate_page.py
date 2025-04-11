from selenium.webdriver.common.by import By
from base_page import BasePage


class RoommatePage(BasePage):
    # Locators
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[placeholder='Search by Name']")
    BUDGET_MIN = (By.XPATH, "//label[contains(text(),'Budget Range')]/following-sibling::div/input[1]")
    BUDGET_MAX = (By.XPATH, "//label[contains(text(),'Budget Range')]/following-sibling::div/input[2]")
    AGE_MIN = (By.XPATH, "//label[contains(text(),'Age Range')]/following-sibling::div/input[1]")
    AGE_MAX = (By.XPATH, "//label[contains(text(),'Age Range')]/following-sibling::div/input[2]")
    GENDER_DROPDOWN = (By.XPATH, "//div[contains(text(),'Gender')]/following-sibling::div")
    RESULT_CARD = (By.CSS_SELECTOR, ".roommate-card")
    RESULT_NAME = (By.CSS_SELECTOR, ".roommate-card h3")

    def search_by_name(self, name):
        self.fill_field(self.SEARCH_FIELD, name)

    def set_budget_range(self, min_val, max_val):
        self.fill_field(self.BUDGET_MIN, str(min_val))
        self.fill_field(self.BUDGET_MAX, str(max_val))

    def set_age_range(self, min_age, max_age):
        self.fill_field(self.AGE_MIN, str(min_age))
        self.fill_field(self.AGE_MAX, str(max_age))

    def select_gender(self, gender):
        self.click_element(self.GENDER_DROPDOWN)
        gender_option = (By.XPATH, f"//div[contains(text(),'{gender}')]")
        self.click_element(gender_option)

    def get_roommate_results(self):
        return self.driver.find_elements(*self.RESULT_CARD)

    def get_roommate_names(self):
        return [el.text for el in self.driver.find_elements(*self.RESULT_NAME)]