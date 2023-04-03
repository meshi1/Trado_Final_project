
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.login_locators import LoginLocators
from time import sleep
from src.utils.db import code

class Loginpage:
    def __init__(self, driver):
        self.driver = driver

    def click_connection_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,LoginLocators.connection_btn ))).click()
        sleep(2)

    def valid_phone(self):
        x = self.driver.find_element(By.XPATH, LoginLocators.phone_input)
        x.send_keys("0523387577")
        return x

    def login_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.login_btn))).click()
        sleep(3)

    def valid_code_and_login(self):
        x = self.driver.find_element(By.XPATH, LoginLocators.code_input)
        v_code= code()
        x.send_keys(v_code)
        sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.validation_btn))).click()
        sleep(2)

    def personal_area(self):
        x = self.driver.find_element(By.XPATH, LoginLocators.user_name)
        sleep(2)
        return x

    def click_Twitter(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.Twitter_btn))).click()
        sleep(2)

    def click_Google(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.Google_btn))).click()
        sleep(2)

    #aseert test 50
    error_google_window = "https://accounts.google.com/signin/oauth/error/v2?authError=ChVyZWRpcmVjdF91cmlfbWlzbWF0Y2gSkgIK15DXmdefINec15og15DXpNep16jXldeqINec15TXmdeb16DXoSDXnNeQ16TXnNeZ16fXpteZ15Qg15TXlteVINeb15kg15TXmdeQINec15Ag16LXldee15PXqiDXkdeT16jXmdep15XXqiDXnteT15nXoNeZ15XXqiBPQXV0aCAyLjAg16nXnCBHb29nbGUuCgrXkNedINeQ16ov15Qg15TXntek16rXly_XqiDXqdecINeU15DXpNec15nXp9em15nXlCwg16LXnNeZ15og15zXqNep15XXnSDXkS1Hb29nbGUgQ2xvdWQgQ29uc29sZSDXkNeqINee16fXldeoINeULUphdmFTY3JpcHQuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2ggkAMqIAoGb3JpZ2luEhZodHRwczovL3FhLnRyYWRvLmNvLmlsMo4DCAESkgIK15DXmdefINec15og15DXpNep16jXldeqINec15TXmdeb16DXoSDXnNeQ16TXnNeZ16fXpteZ15Qg15TXlteVINeb15kg15TXmdeQINec15Ag16LXldee15PXqiDXkdeT16jXmdep15XXqiDXnteT15nXoNeZ15XXqiBPQXV0aCAyLjAg16nXnCBHb29nbGUuCgrXkNedINeQ16ov15Qg15TXntek16rXly_XqiDXqdecINeU15DXpNec15nXp9em15nXlCwg16LXnNeZ15og15zXqNep15XXnSDXkS1Hb29nbGUgQ2xvdWQgQ29uc29sZSDXkNeqINee16fXldeoINeULUphdmFTY3JpcHQuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2g%3D&client_id=918041190286-ts0hq2o9fhq3adumgcj45a3vsp2fh8v9.apps.googleusercontent.com"

    def invalid_phone(self):
        x = self.driver.find_element(By.XPATH, LoginLocators.phone_input)
        x.send_keys("052338757711")
        return x

    #aseert test 51
    def phone_error_message_display(self):
        x = self.driver.find_element(By.XPATH, LoginLocators.phone_error_message)
        return x

    def invalid_code_and_login(self):
        x = self.driver.find_element(By.XPATH, LoginLocators.code_input)
        x.send_keys("00000")
        sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, LoginLocators.validation_btn))).click()
        sleep(2)

    # aseert test 52
    def code_error_message_display(self):
        x = self.driver.find_element(By.XPATH, LoginLocators.code_error_message)
        return x

    def click_logout_btn(self):
        element = self.driver.find_element(By.CLASS_NAME, "header_logOut")
        action = ActionChains(self.driver)
        action.click(on_element=element)
        action.perform()
        sleep(2)

