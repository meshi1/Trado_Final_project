

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.footer_links_locators import Fotter_linksLocators
from time import sleep


class Footer_linkspage:
    def __init__(self, driver):
        self.driver = driver

    def Stay_In_Touch_window_display(self):
        x = self.driver.find_element(By.XPATH, Fotter_linksLocators.Stay_In_Touch_window).is_displayed()
        return x

    def Facebook_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Fotter_linksLocators.Facebook_link))).click()
        sleep(2)

    def Instagram_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Fotter_linksLocators.Instagram_link))).click()
        sleep(2)

    def Additionals_window_display(self):
        x = self.driver.find_element(By.XPATH, Fotter_linksLocators.Additionals_window).is_displayed()
        return x

    def Additional_questions_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Fotter_linksLocators.Additional_questions_link))).click()
        sleep(2)

    def How_does_shipping_work_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Fotter_linksLocators.How_does_shipping_work_link))).click()
        sleep(2)

    def Importants_window_display(self):
        x = self.driver.find_element(By.XPATH, Fotter_linksLocators.Importants_window).is_displayed()
        return x

    def Business_interfaces_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Fotter_linksLocators.Business_interfaces_link))).click()
        sleep(2)

    def Contact_link(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Fotter_linksLocators.Contact_link))).click()
        sleep(2)
