
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.checkout_process_locators import Checkout_processLocators
from time import sleep


class Checkout_processpage:

    def __init__(self, driver):
        self.driver = driver

    def click_payment_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.payment_btn))).click()
        sleep(2)

    def click_checkout_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.checkout_btn))).click()
        sleep(2)

    def click_bank_transfer_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.bank_transfer_btn))).click()
        sleep(2)

    def valid_Bank_transfer_and_pay(self):
        branch = self.driver.find_element(By.XPATH, Checkout_processLocators.branch_input)
        branch.clear()
        branch.send_keys("111")
        acount_number = self.driver.find_element(By.XPATH, Checkout_processLocators.acount_number_input)
        acount_number.clear()
        acount_number.send_keys("112321")
        sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.confirm_btn))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.end_payment_btn))).click()
        sleep(2)

    #assert test 64,65
    def payment_confirmation_text(self):
        x = self.driver.find_element(By.XPATH, Checkout_processLocators.Payment_confirmation_text)
        return x

    def invalid_Bank_transfer_and_pay(self):
        branch = self.driver.find_element(By.XPATH, Checkout_processLocators.branch_input)
        branch.clear()
        branch.send_keys("1111111111111111111111")
        acount_number = self.driver.find_element(By.XPATH, Checkout_processLocators.acount_number_input)
        acount_number.clear()
        acount_number.send_keys("00000000000000000000000000000")
        sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.confirm_btn))).click()
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.end_payment_btn))).click()
        sleep(2)


    def valid_branch(self):
        branch = self.driver.find_element(By.XPATH, Checkout_processLocators.branch_input)
        branch.clear()
        branch.send_keys("111")
        sleep(2)

    def invalid_acount_number(self):
        acount_number = self.driver.find_element(By.XPATH, Checkout_processLocators.acount_number_input)
        acount_number.clear()
        acount_number.send_keys("helloשלום")
        sleep(2)

    def acount_number(self):
        x=  self.driver.find_element(By.XPATH, Checkout_processLocators.acount_number_input)
        return x


    def invalid_branch(self):
        branch = self.driver.find_element(By.XPATH, Checkout_processLocators.branch_input)
        branch.clear()
        branch.send_keys("aaa")
        sleep(2)

    def branch(self):
        x=  self.driver.find_element(By.XPATH, Checkout_processLocators.branch_input)
        return x


    def valid_acount_number(self):
        last_name = self.driver.find_element(By.XPATH, Checkout_processLocators.acount_number_input)
        last_name.clear()
        last_name.send_keys("123456")
        sleep(2)

    def click_credit_card_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, Checkout_processLocators.credit_card_btn))).click()
        sleep(3)

    def valid_credit_and_pay(self):
        num_card = self.driver.find_element(By.CSS_SELECTOR, Checkout_processLocators.input_num_card)
        num_card.send_keys("4580000000000000")
        num_id  = self.driver.find_element(By.XPATH, Checkout_processLocators.input_num_id)
        num_id .clear()
        num_id .send_keys("123456782")
        month_card = self.driver.find_element(By.XPATH, Checkout_processLocators.month_card)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        year_card = self.driver.find_element(By.XPATH, Checkout_processLocators.year_card)
        year_card.send_keys(Keys.ARROW_DOWN)
        year_card.send_keys(Keys.ARROW_DOWN)
        input_ccv_code = self.driver.find_element(By.ID, Checkout_processLocators.input_ccv_code)
        input_ccv_code.clear()
        input_ccv_code.send_keys("123")
        sleep(1)


    #assert test 68
    def message(self):
        x= self.driver.find_element(By.ID, "recaptchaV2-container")
        return x

    def invalid_credit(self):
        num_card = self.driver.find_element(By.CSS_SELECTOR, Checkout_processLocators.input_num_card)
        num_card.send_keys("שלוםשלוםשלום")
        sleep(2)
        num_id  = self.driver.find_element(By.XPATH, Checkout_processLocators.input_num_id)
        num_id .clear()
        num_id .send_keys("123456782")
        month_card = self.driver.find_element(By.XPATH, Checkout_processLocators.month_card)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        month_card.send_keys(Keys.ARROW_DOWN)
        year_card = self.driver.find_element(By.XPATH, Checkout_processLocators.year_card)
        year_card.send_keys(Keys.ARROW_DOWN)
        year_card.send_keys(Keys.ARROW_DOWN)
        input_ccv_code = self.driver.find_element(By.ID, Checkout_processLocators.input_ccv_code)
        input_ccv_code.clear()
        input_ccv_code.send_keys("123")
        sleep(3)

    #assert test 69
    def error_message_card(self):
        x = self.driver.find_element(By.ID, Checkout_processLocators.error_message_card)
        return  x



