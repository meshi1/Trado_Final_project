

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.locators.registration_locators import RegistrationLocators
from time import sleep
from src.utils.db import loop_for_valid_phone
from src.utils.db import get_specific_key_value_2



class Registrationpage:
    def __init__(self, driver):
        self.driver = driver

    def click_connection_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,RegistrationLocators.connection_btn ))).click()
        sleep(2)

    def click_registration_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH,RegistrationLocators.registration_btn ))).click()
        sleep(2)

    def loop_for_valid_phone(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.phone_input)
        phone = loop_for_valid_phone()
        x.send_keys(phone)
        return phone

    def valid_code_and_login(self, phone):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.code_input)
        v_code = get_specific_key_value_2(phone)
        x.send_keys(v_code)
        sleep(2)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RegistrationLocators.validation_btn))).click()
        sleep(2)

    def valid_num_HF_EM(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.HF_EM_input)
        x.send_keys("1113")
        return x

    def click_restaurants_and_save(self):
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH,RegistrationLocators.restaurants_btn))).click()
        WebDriverWait(self.driver, 5)
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RegistrationLocators.creat_acount_btn))).click()
        sleep(1)

    def personal_area(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.user_name)
        sleep(2)
        return x

    def exists_user_phone(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.phone_input)
        x.send_keys("0523387577")
        return x

    def exists_num_HF_EM(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.HF_EM_input)
        x.send_keys("111")
        return x

    def Accept_regulations(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RegistrationLocators.Accept_regulations))).click()
        sleep(2)

    def click_login_btn(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RegistrationLocators.login_btn))).click()
        sleep(2)

    #assert test 41
    def error_message_display(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.error_message)
        return x

    def click_Twitter(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RegistrationLocators.Twitter_btn))).click()
        sleep(2)

    def click_Google(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, RegistrationLocators.Google_btn))).click()
        sleep(2)

    def invalid_phone(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.phone_input)
        x.send_keys("05233875777")
        sleep(2)
        return x

    #assert test 43
    def phone_error_message_display(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.phone_error_message)
        return x

    def valid_phone(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.phone_input)
        x.send_keys("0523387577")
        sleep(2)
        return x

    def invalid_HF_EM(self, num ):
        self.driver.find_element(By.XPATH,RegistrationLocators.HF_EM_input).send_keys(num)

    def valid_HF_EM(self):
        x = self.driver.find_element(By.XPATH,RegistrationLocators.HF_EM_input)
        x.send_keys("12345")
        sleep(2)


    #assert test 46
    def privacy_policy_error_message_display(self):
        x = self.driver.find_element(By.XPATH, RegistrationLocators.privacy_policy_error_message)
        return x

    #assert test 43
    error_google_window = "https://accounts.google.com/signin/oauth/error/v2?authError=ChVyZWRpcmVjdF91cmlfbWlzbWF0Y2gSkgIK15DXmdefINec15og15DXpNep16jXldeqINec15TXmdeb16DXoSDXnNeQ16TXnNeZ16fXpteZ15Qg15TXlteVINeb15kg15TXmdeQINec15Ag16LXldee15PXqiDXkdeT16jXmdep15XXqiDXnteT15nXoNeZ15XXqiBPQXV0aCAyLjAg16nXnCBHb29nbGUuCgrXkNedINeQ16ov15Qg15TXntek16rXly_XqiDXqdecINeU15DXpNec15nXp9em15nXlCwg16LXnNeZ15og15zXqNep15XXnSDXkS1Hb29nbGUgQ2xvdWQgQ29uc29sZSDXkNeqINee16fXldeoINeULUphdmFTY3JpcHQuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2ggkAMqIAoGb3JpZ2luEhZodHRwczovL3FhLnRyYWRvLmNvLmlsMo4DCAESkgIK15DXmdefINec15og15DXpNep16jXldeqINec15TXmdeb16DXoSDXnNeQ16TXnNeZ16fXpteZ15Qg15TXlteVINeb15kg15TXmdeQINec15Ag16LXldee15PXqiDXkdeT16jXmdep15XXqiDXnteT15nXoNeZ15XXqiBPQXV0aCAyLjAg16nXnCBHb29nbGUuCgrXkNedINeQ16ov15Qg15TXntek16rXly_XqiDXqdecINeU15DXpNec15nXp9em15nXlCwg16LXnNeZ15og15zXqNep15XXnSDXkS1Hb29nbGUgQ2xvdWQgQ29uc29sZSDXkNeqINee16fXldeoINeULUphdmFTY3JpcHQuCiAgGnVodHRwczovL2RldmVsb3BlcnMuZ29vZ2xlLmNvbS9pZGVudGl0eS9wcm90b2NvbHMvb2F1dGgyL2phdmFzY3JpcHQtaW1wbGljaXQtZmxvdyNhdXRob3JpemF0aW9uLWVycm9ycy1vcmlnaW4tbWlzbWF0Y2g%3D&client_id=918041190286-ts0hq2o9fhq3adumgcj45a3vsp2fh8v9.apps.googleusercontent.com"
    #assert test 47
    privacy_policy_window = "https://qa.trado.co.il/info/%D7%9E%D7%93%D7%99%D7%A0%D7%99%D7%95%D7%AA%20%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA"
