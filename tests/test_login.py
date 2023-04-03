
from src.utils.setup import WebDriverSetup
import allure

class TestTORADO(WebDriverSetup):

    @allure.title("test_48_valid_login")
    def test_48_valid_login(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        text = self.login_page.personal_area().text
        assert text == "אזור אישי"

    @allure.title("test_49_valid_login_Twitter")
    def test_49_valid_login_Twitter(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.click_Twitter()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url != "about:blank"

    @allure.title("test_50_valid_login_Google")
    def test_50_valid_login_Google(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.click_Google()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url != self.login_page.error_google_window

    @allure.title("test_51_invalid_login_phone_num")
    def test_51_invalid_login_phone_num(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.invalid_phone()
        self.login_page.login_btn()
        assert self.login_page.phone_error_message_display()

    @allure.title("test_52_invalid_login_code_num")
    def test_52_invalid_login_code_num(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.invalid_code_and_login()
        assert self.login_page.phone_error_message_display()

    @allure.title("test_53_logout")
    def test_53_logout(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.login_page.click_logout_btn()
        text = self.login_page.personal_area().text
        assert text == "התחברות"
