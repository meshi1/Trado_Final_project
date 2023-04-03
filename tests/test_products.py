
from src.utils.setup import WebDriverSetup
import allure

class TestTORADO(WebDriverSetup):

    @allure.title("test_33_add_single_product_to_cart")
    def test_33_add_single_product_to_cart(self, setUp):
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        assert self.products_page.product_1_add_cart()

    @allure.title("test_34_removing_product")
    def test_34_removing_product(self, setUp):
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        self.products_page.click_removing()
        assert self.products_page.product_1_removing_cart()

    @allure.title("test_35_add_few_products_to_cart")
    def test_35_add_few_products_to_cart(self, setUp):
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        assert self.products_page.product_1_add_cart()
        self.home_page.click_logo_btn()
        self.products_page.click_product_2_btn()
        self.products_page.click_add_product_2()
        assert self.products_page.product_2_add_cart()

    @allure.title("test_36_title_product_main_to_title_product_page")
    def test_36_title_product_main_to_title_product_page(self, setUp):
        internal = self.products_page.text_product_1_btn().text
        self.products_page.click_product_1_btn()
        external = self.products_page.text_page_product_1().text
        assert internal == external

    @allure.title("test_37_title_quantity_stock_main_to_title_quantity_stock_product_page")
    def test_37_title_quantity_stock_main_to_title_quantity_stock_product_page(self, setUp):
        internal = self.products_page.text_quantity_stock_main().text
        self.products_page.click_product_1_btn()
        external = self.products_page.text_quantity_stock_product_page().get_attribute("innerText")
        assert internal == external

    @allure.title("test_38_price_product_page_to_price_product_cart")
    def test_38_price_product_page_to_price_product_cart(self, setUp):
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        price_page = self.products_page.price_product_page().text
        price_cart = self.products_page.price_product_cart().text
        assert price_page == price_cart

    @allure.title("test_39_quantity_bar_of_the_product_to_minimum_order")
    def test_39_quantity_bar_of_the_product_to_minimum_order(self, setUp):
        self.products_page.click_product_3_btn()
        self.products_page.click_add_product_3()
        quantity_bar= self.products_page.text_quantity_bar_product_3().text
        quantity_minimum_order = self.products_page.text_quantity_minimum_order().text
        assert quantity_bar in quantity_minimum_order
