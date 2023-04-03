
from src.utils.setup import WebDriverSetup
from time import sleep
import allure

class TestTORADO(WebDriverSetup):

    @allure.title("test_54_personal_area_btn")
    def test_54_personal_area_btn(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        assert self.driver.current_url == "https://qa.trado.co.il/user/personalArea"

    @allure.title("test_55_My_wallet_window_display")
    def test_55_My_wallet_window_display(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        assert self.personal_area_page.My_wallet_window_display()

    @allure.title("test_56_Products_arena_window_display")
    def test_56_Products_arena_window_display(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        assert self.personal_area_page.Products_arena_window_display()

    @allure.title("test_57_Previous_Orders_window_display")
    def test_57_Previous_Orders_window_display(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        assert self.personal_area_page.Previous_Orders_window_display()

    @allure.title("test_58_link_Previous_Orders_window")
    def test_58_link_Previous_Orders_window(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        self.personal_area_page.click_link_Previous_Orders()
        assert self.driver.current_url == "https://qa.trado.co.il/contact"

    @allure.title("test_59_Orders_for_collection_window_display")
    def test_59_Orders_for_collection_window_display(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        assert self.personal_area_page.Previous_Orders_for_collection_display()

    @allure.title("test_60_link_Orders_for_collection_window")
    def test_60_link_Orders_for_collection_window(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        self.personal_area_page.click_link_Orders_for_collection()
        assert self.driver.current_url == "https://qa.trado.co.il/contact"

    @allure.title("test_61_Delivery_details_window_display")
    def test_61_Delivery_details_window_display(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        assert self.personal_area_page.Delivery_details_window_display()

    @allure.title("test_62_valid_Delivery_details")
    def test_62_valid_Delivery_details(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        self.personal_area_page.click_Edit_btn()
        self.personal_area_page.valid_Delivery_details_and_save()
        sleep(2)
        text_first_name = self.personal_area_page.first_name().get_attribute("value")
        text_last_name = self.personal_area_page.last_name().get_attribute("value")
        text_phone = self.personal_area_page.phone().get_attribute("value")
        text_mail = self.personal_area_page.mail().get_attribute("value")
        text_HF_num = self.personal_area_page.HF_num().get_attribute("value")
        text_street_number = self.personal_area_page.street_number().get_attribute("value")
        text_street_city = self.personal_area_page.street_city().get_attribute("value")
        assert  text_first_name == "משי" and text_phone == "0523387577" \
                and text_last_name == "גל" and text_mail == "diyoda9320@huvacliq.com" \
                and text_HF_num == "997" and text_street_number == "5" \
                and text_street_city == "הדרום"

    @allure.title("test_63_invalid_delivery_details_first_name_empty")
    def test_63_invalid_delivery_details_first_name_empty(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.personal_area_page.click_personal_area_btn()
        self.personal_area_page.click_Edit_btn()
        self.personal_area_page.valid_delivery_details_without_first_name()
        error_message = self.personal_area_page.error_message().get_attribute("innerText")
        sleep(2)
        assert error_message == "נא למלא שדה זה"
