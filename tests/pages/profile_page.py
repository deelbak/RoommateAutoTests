from selenium.webdriver.common.by import By
from .base_page import BasePage


class ProfilePage(BasePage):
    # Locators
    PHOTO_UPLOAD_INPUT = (By.CSS_SELECTOR, "input[type='file']")
    SAVE_PHOTO_BTN = (By.XPATH, "//button[contains(text(),'Save photo')]")
    CANCEL_PHOTO_BTN = (By.XPATH, "//button[contains(text(),'Cancel')]")
    PROFILE_IMAGE = (By.CSS_SELECTOR, ".profile-image img")
    TOAST_MESSAGE = (By.CSS_SELECTOR, ".toast-message")

    def upload_profile_photo(self, file_path):
        """Uploads a profile photo from given file path"""
        self.driver.find_element(*self.PHOTO_UPLOAD_INPUT).send_keys(file_path)

    def save_photo(self):
        """Clicks Save Photo button"""
        self.click_element(self.SAVE_PHOTO_BTN)

    def cancel_photo(self):
        """Clicks Cancel button"""
        self.click_element(self.CANCEL_PHOTO_BTN)

    def get_toast_message(self):
        """Returns the toast notification text"""
        return self.find_element(self.TOAST_MESSAGE).text

    def is_profile_image_visible(self):
        """Checks if profile image is displayed"""
        return self.driver.find_element(*self.PROFILE_IMAGE).is_displayed()