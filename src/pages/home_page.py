
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.home_locators import HomeLocators
from time import sleep


class Homepage:
    def __init__(self, driver):
        self.driver = driver


    def click_restaurants_and_save(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,HomeLocators.restaurants_btn))).click()
        WebDriverWait(self.driver, 5)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.save_btn))).click()
        sleep(1)

    def txt_Promotions_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Promotions_btn)))
        return title

    def txt_Canabis_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Canabis_btn)))
        return title

    def txt_Drinks_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Drinks_btn)))
        return title

    def txt_New_product_upload_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.New_product_upload_btn)))
        return title

    def txt_Login_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Login_btn)))
        return title

    def click_Promotions_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Promotions_btn))).click()


    def click_Canabis_btn(self):
        title = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Canabis_btn))).click()
        return title

    def click_Drinks_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Drinks_btn))).click()

    def click_Login_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Login_btn))).click()

    #assert test 9
    def pop_up_Login(self):
        x= WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.pop_up_Login)))
        return x

    def click_logo_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.logo_btn))).click()
        sleep(2)

    # assert test 11
    def image_logo_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.image_logo).is_displayed()
        return x

    def click_image_bar_right_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.image_bar_right_btn))).click()
        sleep(3)

    def click_image_bar_left_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.image_bar_left_btn))).click()
        sleep(3)


    #assert test 12-13
    def image_1_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.image_1).is_displayed()
        return x

    def image_2_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.image_2).is_displayed()
        return x

    def image_3_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.image_3).is_displayed()
        return x

    # assert test 16
    def Shopping_Cart_window_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.Shopping_Cart_window).is_displayed()
        return x

    # assert test 17
    def Max_Business_window_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.Max_Business_window).is_displayed()
        return x

    def click_Max_Business_window_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Max_Business_window_link))).click()

    # assert test 19
    def Common_questions_window_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.Common_questions).is_displayed()
        return x

    def click_Common_questions_window_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Common_questions_link))).click()
        sleep(2)

    # assert test 21
    def Contact_window_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.Contact_window).is_displayed()
        return x

    def click_Contact_window_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.Contact_link))).click()
        sleep(2)

    # assert test 23
    def How_does_shipping_work_window_display(self):
        x = self.driver.find_element(By.XPATH, HomeLocators.How_does_shipping_work).is_displayed()
        return x

    def click_How_does_shipping_work_window_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, HomeLocators.How_does_shipping_work_link))).click()
        sleep(2)
