

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.personal_area_locators import Personal_AreaLocators
from time import sleep


class Personal_areapage:
    def __init__(self, driver):
        self.driver = driver

    def click_personal_area_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Personal_AreaLocators.personal_area_btn))).click()
        sleep(2)

    #assert test 55
    def My_wallet_window_display(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.My_wallet_window).is_displayed()
        return x

    #assert test 56
    def Products_arena_window_display(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.Products_arena_window).is_displayed()
        return x

    #assert test 57
    def Previous_Orders_window_display(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.Previous_Orders_window).is_displayed()
        return x

    def click_link_Previous_Orders(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Personal_AreaLocators.link_Previous_Orders))).click()
        sleep(2)

   #assert test 59
    def Previous_Orders_for_collection_display(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.Orders_for_collection_window).is_displayed()
        return x

    def click_link_Orders_for_collection(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Personal_AreaLocators.link_Orders_for_collection))).click()
        sleep(2)

    #assert 61 test
    def Delivery_details_window_display(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.Delivery_details_window).is_displayed()
        return x

    def click_Edit_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Personal_AreaLocators.Edit_btn))).click()
        sleep(2)

    def valid_Delivery_details_and_save(self):
        first_name = self.driver.find_element(By.XPATH, Personal_AreaLocators.first_name)
        first_name.clear()
        first_name.send_keys("משי")
        last_name = self.driver.find_element(By.XPATH, Personal_AreaLocators.last_name)
        last_name.clear()
        last_name.send_keys("גל")
        sleep(2)
        phone = self.driver.find_element(By.XPATH, Personal_AreaLocators.phone)
        phone.clear()
        phone.send_keys("0523387577")
        sleep(2)
        mail= self.driver.find_element(By.XPATH, Personal_AreaLocators.mail)
        mail.clear()
        mail.send_keys("diyoda9320@huvacliq.com")
        HF_num = self.driver.find_element(By.XPATH, Personal_AreaLocators.HF_num)
        HF_num.clear()
        HF_num.send_keys("997")
        street_number = self.driver.find_element(By.XPATH, Personal_AreaLocators.street_number)
        street_number.clear()
        street_number.send_keys("5")
        sleep(5)
        street_city =  self.driver.find_element(By.XPATH, Personal_AreaLocators.street_city)
        street_city.clear()
        street_city.send_keys("הדרום")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Personal_AreaLocators.save_btn))).click()
        sleep(2)

    #assert 62 test

    def first_name(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.first_name)
        return x

    def last_name(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.last_name)
        return x

    def phone(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.phone)
        return x

    def mail(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.mail)
        return x

    def HF_num(self):
        x =  self.driver.find_element(By.XPATH, Personal_AreaLocators.HF_num)
        return x

    def street_number(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.street_number)
        return x

    def street_city(self):
        x = self.driver.find_element(By.XPATH, Personal_AreaLocators.street_city)
        return x

    def valid_delivery_details_without_first_name(self):
        first_name = self.driver.find_element(By.XPATH, Personal_AreaLocators.first_name)
        first_name.clear()
        last_name = self.driver.find_element(By.XPATH, Personal_AreaLocators.last_name)
        last_name.clear()
        last_name.send_keys("גל")
        phone = self.driver.find_element(By.XPATH, Personal_AreaLocators.phone)
        phone.clear()
        phone.send_keys("0523387577")
        sleep(2)
        mail= self.driver.find_element(By.XPATH, Personal_AreaLocators.mail)
        mail.clear()
        mail.send_keys("diyoda9320@huvacliq.com")
        HF_num = self.driver.find_element(By.XPATH, Personal_AreaLocators.HF_num)
        HF_num.clear()
        HF_num.send_keys("997")
        street_number = self.driver.find_element(By.XPATH, Personal_AreaLocators.street_number)
        street_number.clear()
        street_number.send_keys("5")
        sleep(2)
        street_city =  self.driver.find_element(By.XPATH, Personal_AreaLocators.street_city)
        street_city.clear()
        street_city.send_keys("הדרום")


    def error_message(self):
        x = self.driver.find_element(By.CLASS_NAME, Personal_AreaLocators.error_message)
        return x