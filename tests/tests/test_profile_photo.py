import pytest
import os
from tests.pages.profile_page import ProfilePage

@pytest.mark.usefixtures("setup")
class TestProfilePhotoUpload:
    @pytest.fixture
    def profile_page(self, setup):
        return ProfilePage(setup)

    def test_successful_photo_upload(self, profile_page):
        """Test successful profile photo upload"""
        test_photo = os.path.join(os.path.dirname(__file__), "..", "test_data", "test_photo.jpg")

        profile_page.upload_profile_photo(test_photo)
        profile_page.save_photo()

        assert "Photo uploaded successfully" in profile_page.get_toast_message()
        assert profile_page.is_profile_image_visible()

    def test_cancel_photo_upload(self, profile_page):
        """Test canceling photo upload"""
        test_photo = os.path.join(os.path.dirname(__file__), "..", "test_data", "test_photo.jpg")

        profile_page.upload_profile_photo(test_photo)
        profile_page.cancel_photo()

        assert not profile_page.is_profile_image_visible()

    @pytest.mark.parametrize("file_type", ["jpg", "png"])
    def test_different_file_types(self, profile_page, file_type):
        """Test uploading different image file types"""
        test_file = os.path.join(os.path.dirname(__file__), "..", "test_data", f"test_photo.{file_type}")

        profile_page.upload_profile_photo(test_file)
        profile_page.save_photo()

        assert profile_page.is_profile_image_visible()