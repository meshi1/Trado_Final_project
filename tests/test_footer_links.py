
import allure
from src.utils.setup import WebDriverSetup

class TestTORADO(WebDriverSetup):

    @allure.title("test_25_Stay_In_Touch_window_display")
    def test_25_Stay_In_Touch_window_display(self, setUp):
        assert self.footer_links_page.Stay_In_Touch_window_display()

    @allure.title("test_26_External_link_Stay_In_Touch_window_Facebook")
    def test_26_External_link_Stay_In_Touch_window_Facebook_and_Instagram(self, setUp):
        self.footer_links_page.Stay_In_Touch_window_display()
        self.footer_links_page.Facebook_link()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == ("https://www.facebook.com/")

    @allure.title("test_26_External_link_Stay_In_Touch_window_Instagram")
    def test_26_External_link_Stay_In_Touch_window_Instagram(self, setUp):
        self.footer_links_page.Stay_In_Touch_window_display()
        self.footer_links_page.Instagram_link()
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert self.driver.current_url == "https://www.instagram.com/"

    @allure.title("test_27_Additionals_window_display")
    def test_27_Additionals_window_display(self, setUp):
        assert self.footer_links_page.Additionals_window_display()

    @allure.title("test_28_Internal_link_Additionals_window")
    def test_28_Internal_link_Additionals_window(self, setUp):
        self.footer_links_page.Additionals_window_display()
        self.footer_links_page.Additional_questions_link()
        assert self.driver.current_url == "https://qa.trado.co.il/questions"
        self.home_page.click_logo_btn()
        self.footer_links_page.How_does_shipping_work_link()
        assert self.driver.current_url == "https://qa.trado.co.il/shipment"

    @allure.title("test_29_Importants_window_display")
    def test_29_Importants_window_display(self, setUp):
        assert self.footer_links_page.Importants_window_display()

    @allure.title("test_30_Internal_link_Importants_window_Business_interfaces_Contact")
    def test_30_Internal_link_Importants_window_Business_interfaces_Contact(self, setUp):
        self.footer_links_page.Importants_window_display()
        self.footer_links_page.Contact_link()
        assert self.driver.current_url == "https://qa.trado.co.il/contact"
        self.home_page.click_logo_btn()
        self.footer_links_page.Business_interfaces_link()
        assert self.driver.current_url == "https://qa.trado.co.il/joinUs"