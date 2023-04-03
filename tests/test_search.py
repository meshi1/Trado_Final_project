
from src.utils.setup import WebDriverSetup
import allure

class TestTORADO(WebDriverSetup):

    @allure.title("valid_search")
    def test_31_valid_search(self,setUp):
        self.search_page.valid_search()
        results_text = self.search_page.search_results()
        assert results_text.text == "2 תוצאות"

    def test_32_invalid_search(self,setUp):
        self.search_page.invalid_search()
        results_text = self.search_page.search_results()
        assert results_text.text == "0 תוצאות"
