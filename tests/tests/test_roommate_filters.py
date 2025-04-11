import pytest

from ..pages.roommate_page import RoommatePage

@pytest.mark.usefixtures("setup")
class TestRoommateFilters:
    def test_search_by_name(self, setup):
        driver = setup
        roommate_page = RoommatePage(driver)
        roommate_page.search_by_name("Itachi Uchiha")
        results = roommate_page.get_roommate_names()
        assert "Itachi Uchiha" in results

    def test_budget_filter(self, setup):
        driver = setup
        roommate_page = RoommatePage(driver)
        roommate_page.set_budget_range(50600, 65000)
        results = roommate_page.get_roommate_results()
        assert len(results) > 0

    @pytest.mark.parametrize("age_range", [(20, 30), (24, 24)])
    def test_age_filter(self, setup, age_range):
        driver = setup
        roommate_page = RoommatePage(driver)
        min_age, max_age = age_range
        roommate_page.set_age_range(min_age, max_age)
        results = roommate_page.get_roommate_results()
        assert len(results) > 0

    @pytest.mark.parametrize("gender", ["Male", "Female", "Any"])
    def test_gender_filter(self, setup, gender):
        driver = setup
        roommate_page = RoommatePage(driver)
        roommate_page.select_gender(gender)
        results = roommate_page.get_roommate_results()
        assert len(results) > 0