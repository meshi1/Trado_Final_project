
from src.utils.setup import WebDriverSetup
import allure

class TestTORADO(WebDriverSetup):

    @allure.title("test_4O_valid_registration")
    def test_4O_valid_registration(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        phone = self.registration_page.loop_for_valid_phone()
        self.registration_page.valid_HF_EM()
        self.registration_page.Accept_regulations()
        self.registration_page.click_login_btn()
        self.registration_page.valid_code_and_login(phone)
        self.registration_page.click_restaurants_and_save()
        text = self.registration_page.personal_area().text
        assert text == "אזור אישי"

    @allure.title("test_41_registration_with_exists_user")
    def test_41_registration_with_exists_user(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        self.registration_page.exists_user_phone()
        self.registration_page.exists_num_HF_EM()
        self.registration_page.Accept_regulations()
        self.registration_page.click_login_btn()
        error_m= self.registration_page.error_message_display().get_attribute("innerText")
        assert error_m == "שדה צריך להיות ייחודיי"

    @allure.title("test_42_valid_Registration_with_Twitter")
    def test_42_valid_Registration_with_Twitter(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        self.registration_page.click_Twitter()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url != "about:blank"

    @allure.title("test_43_valid_Registration_with_Google")
    def test_43_valid_Registration_with_Google(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        self.registration_page.click_Google()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url != self.registration_page.error_google_window

    @allure.title("test_44_invalid_phone_number")
    def test_44_invalid_phone_number(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        self.registration_page.invalid_phone()
        error_m = self.registration_page.phone_error_message_display().text
        assert error_m == "מס׳ טלפון לא תקין"

    @allure.title("test_45_invalid_HF_EM_number")
    def test_45_invalid_HF_EM_number(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        self.registration_page.valid_phone()
        num_HF_EM = "1234567891"
        self.registration_page.invalid_HF_EM(num_HF_EM)
        assert len(num_HF_EM) <= 9

    @allure.title("test_46_un_accept_privacy_policy")
    def test_46_un_accept_privacy_policy(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        self.registration_page.valid_phone()
        self.registration_page.valid_HF_EM()
        self.registration_page.click_login_btn()
        error_m = self.registration_page.privacy_policy_error_message_display().text
        assert error_m == "Please Approve Our Policy"

    @allure.title("test_47_privacy_policy_link")
    def test_47_privacy_policy_link(self, setUp):
        self.registration_page.click_connection_btn()
        self.registration_page.click_registration_btn()
        self.registration_page.Accept_regulations()
        assert self.driver.current_url == self.registration_page.privacy_policy_window
