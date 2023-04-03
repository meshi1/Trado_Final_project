

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.search_locators import SearchLocators
from time import sleep

class Searchpage:
    def __init__(self, driver):
        self.driver = driver

    def valid_search(self):
        x = self.driver.find_element(By.XPATH, SearchLocators.search)
        x.send_keys("Goats")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,SearchLocators.Promotions_btn))).click()
        sleep(2)
        x.click()
        sleep(2)

    def invalid_search(self):
        x = self.driver.find_element(By.XPATH, SearchLocators.search)
        x.send_keys("what")
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, SearchLocators.Promotions_btn))).click()
        sleep(2)
        x.click()
        sleep(2)

    #assert test 31-32
    def search_results(self):
        x= self.driver.find_element(By.XPATH,SearchLocators.results_search)
        return x



