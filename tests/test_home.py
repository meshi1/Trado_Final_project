
import allure
from src.utils.setup import WebDriverSetup

class TestTORADO(WebDriverSetup):

    @allure.title("test_1_text_Promotions_btn")
    def test_1_text_Promotions_btn(self, setUp):
        button = self.home_page.txt_Promotions_btn()
        assert button.text == "מבצעים"

    @allure.title("test_2_text_Canabis_btn")
    def test_2_text_Canabis_btn(self, setUp):
        button = self.home_page.txt_Canabis_btn()
        assert button.text == "קנאביס"

    @allure.title("test_3_text_Drinks_btn")
    def test_3_text_Drinks_btn(self, setUp):
        button = self.home_page.txt_Drinks_btn()
        assert button.text == "משקאות"

    @allure.title("test_4_text_New_product_upload_btn")
    def test_4_text_New_product_upload_btn(self, setUp):
        button = self.home_page.txt_New_product_upload_btn()
        assert button.text == "+ העלאת מוצר חדש"

    @allure.title("test_5_text_Login_btn")
    def test_5_text_Login_btn(self, setUp):
        button = self.home_page.txt_Login_btn()
        assert button.text == "התחברות"

    @allure.title("test_6_click_Promotions_btn")
    def test_6_click_Promotions_btn(self, setUp):
        self.home_page.click_Promotions_btn()
        assert self.driver.current_url == "https://qa.trado.co.il/"

    @allure.title("test_7_click_Canabis_btn")
    def test_7_click_Canabis_btn(self, setUp):
        self.home_page.click_Canabis_btn()
        assert self.driver.current_url == "https://qa.trado.co.il/?sectionName=%D7%A7%D7%A0%D7%90%D7%91%D7%99%D7%A1"

    @allure.title("test_8_click_Drinks_btn")
    def test_8_click_Drinks_btn(self, setUp):
        self.home_page.click_Drinks_btn()
        assert self.driver.current_url == "https://qa.trado.co.il/?sectionName=%D7%9E%D7%A9%D7%A7%D7%90%D7%95%D7%AA"

    @allure.title("test_9_click_Login_btn")
    def test_9_click_Login_btn(self, setUp):
        self.home_page.click_Login_btn()
        assert self.home_page.pop_up_Login()

    @allure.title("test_10_click_logo_btn")
    def test_10_click_logo_btn(self, setUp):
        self.home_page.click_Login_btn()
        assert self.driver.current_url == "https://qa.trado.co.il/"

    @allure.title("test_11_image_logo")
    def test_11_image_logo(self, setUp):
        assert self.home_page.image_logo_display()

    @allure.title("test_12_image_bar_right_btn")
    def test_12_image_bar_right_btn(self, setUp):
        assert self.home_page.image_1_display()
        self.home_page.click_image_bar_right_btn()
        assert self.home_page.image_2_display()

    @allure.title("test_13_image_bar_left_btn")
    def test_13_image_bar_left_btn(self, setUp):
        assert self.home_page.image_1_display()
        self.home_page.click_image_bar_left_btn()
        assert self.home_page.image_3_display()

    @allure.title("test_16_My_Shopping_Cart_window_display")
    def test_16_My_Shopping_Cart_window_display(self, setUp):
        assert self.home_page.Shopping_Cart_window_display()

    @allure.title("test_17_Max_Business_window_display")
    def test_17_Max_Business_window_display(self, setUp):
        assert self.home_page.Max_Business_window_display()

    @allure.title("test_18_Max_Business_window_link")
    def test_18_Max_Business_window_link(self, setUp):
        self.home_page.Max_Business_window_display()
        self.home_page.click_Max_Business_window_link()
        assert self.driver.current_url != "https://qa.trado.co.il/"

    @allure.title("test_19_Common_questions_window_display")
    def test_19_Common_questions_window_display(self, setUp):
        assert self.home_page.Common_questions_window_display()

    @allure.title("test_20_Common_questions_window_link")
    def test_20_Common_questions_window_link(self, setUp):
        self.home_page.Common_questions_window_display()
        self.home_page.click_Common_questions_window_link()
        assert self.driver.current_url == "https://qa.trado.co.il/questions"

    @allure.title("test_21_Common_questions_window_display")
    def test_21_Common_questions_window_display(self, setUp):
        assert self.home_page.Contact_window_display()

    @allure.title("test_22_Common_questions_window_link")
    def test_22_Common_questions_window_link(self, setUp):
        self.home_page.Contact_window_display()
        self.home_page.click_Contact_window_link()
        assert self.driver.current_url == "https://qa.trado.co.il/contact"

    @allure.title("test_23_How_does_shipping_work_window_display")
    def test_23_How_does_shipping_work_window_display(self, setUp):
        assert self.home_page.How_does_shipping_work_window_display()

    @allure.title("test_24_How_does_shipping_work_window_link")
    def test_24_How_does_shipping_work_window_link(self, setUp):
        self.home_page.How_does_shipping_work_window_display()
        self.home_page.click_How_does_shipping_work_window_link()
        assert self.driver.current_url == "https://qa.trado.co.il/shipment"
