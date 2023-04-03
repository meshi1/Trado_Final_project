
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.products_locators import ProductsLocators
from time import sleep


class Productspage:
    def __init__(self, driver):
        self.driver = driver

    def click_product_1_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.product_1_btn ))).click()

    def click_add_product_1(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.add_product ))).click()
        sleep(2)

    #assert test 33
    def product_1_add_cart(self):
        x =  WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.product_1_cart )))
        return x

    def click_removing(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.removing_product ))).click()
        sleep(2)

    #assert test 34
    def product_1_removing_cart(self):
        x =  WebDriverWait(self.driver, 5).until(
            EC.invisibility_of_element_located((By.XPATH,ProductsLocators.product_1_cart )))
        return x

    def click_product_2_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.product_2_btn ))).click()

    def click_add_product_2(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.add_product ))).click()

    #assert test 35
    def product_2_add_cart(self):
        x =  WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.product_2_cart )))
        return x

    def text_product_1_btn(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.text_product_1_btn )))
        return x

    def text_page_product_1(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.text_page_product_1 )))
        return x

    def text_quantity_stock_main(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.text_quantity_stock_main)))
        return x

    def text_quantity_stock_product_page(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.text_quantity_stock_product_page)))
        return x

    def price_product_page(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.price_product_page)))
        return x

    def price_product_cart(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.price_product_cart)))
        return x

    def click_product_3_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.product_3_btn ))).click()
        sleep(2)

    def click_add_product_3(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,ProductsLocators.add_product ))).click()
        sleep(2)

    def text_quantity_bar_product_3(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.text_quantity_bar_product_3)))
        return x

    def text_quantity_minimum_order(self):
        x = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, ProductsLocators.text_quantity_minimum_order)))
        return x