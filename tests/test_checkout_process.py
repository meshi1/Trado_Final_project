

from src.utils.setup import WebDriverSetup
import allure

class TestTORADO(WebDriverSetup):

    @allure.title("test_64_valid_bank_transfer")
    def test_64_valid_bank_transfer(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        self.checkout_process_page.click_payment_btn()
        self.checkout_process_page.click_checkout_btn()
        self.checkout_process_page.click_bank_transfer_btn()
        self.checkout_process_page.valid_Bank_transfer_and_pay()
        text = self.checkout_process_page.payment_confirmation_text().get_attribute("outerText")
        assert text == "תודה שהזמנת דרכנו!"

    @allure.title("test_65_invalid_bank_transfer")
    def test_65_invalid_bank_transfer(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        self.checkout_process_page.click_payment_btn()
        self.checkout_process_page.click_checkout_btn()
        self.checkout_process_page.click_bank_transfer_btn()
        self.checkout_process_page.invalid_Bank_transfer_and_pay()
        text = self.checkout_process_page.payment_confirmation_text().get_attribute("outerText")
        assert text != "תודה שהזמנת דרכנו!"

    @allure.title("test_66_invalid_bank_transfer_String_in_the_acount_number")
    def test_66_invalid_bank_transfer_String_in_the_acount_number(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        self.checkout_process_page.click_payment_btn()
        self.checkout_process_page.click_checkout_btn()
        self.checkout_process_page.click_bank_transfer_btn()
        self.checkout_process_page.valid_branch()
        self.checkout_process_page.invalid_acount_number()
        acount_number = self.checkout_process_page.acount_number().get_attribute("value")
        assert acount_number.isnumeric() == True

    @allure.title("test_67_invalid_bank_transfer_String_in_the_branch")
    def test_67_invalid_bank_transfer_String_in_the_branch(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        self.checkout_process_page.click_payment_btn()
        self.checkout_process_page.click_checkout_btn()
        self.checkout_process_page.click_bank_transfer_btn()
        self.checkout_process_page.valid_acount_number()
        self.checkout_process_page.invalid_branch()
        branch = self.checkout_process_page.branch().get_attribute("value")
        assert branch.isnumeric() == True

    @allure.title("test_68_valid_Payment_by_credit")
    def test_68_valid_Payment_by_credit(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        self.checkout_process_page.click_payment_btn()
        self.checkout_process_page.click_checkout_btn()
        self.checkout_process_page.click_credit_card_btn()
        self.driver.switch_to.frame("yaadFrame")
        self.checkout_process_page.valid_credit_and_pay()
        text = self.checkout_process_page.message().get_attribute("innerText")
        assert text != "לצורכי אבטחה, יש לעבור תהליך אימות בטרם מעבר לדף התשלום"


    @allure.title("test_69_invalid_Payment_by_credit")
    def test_69_invalid_Payment_by_credit(self, setUp):
        self.login_page.click_connection_btn()
        self.login_page.valid_phone()
        self.login_page.login_btn()
        self.login_page.valid_code_and_login()
        self.products_page.click_product_1_btn()
        self.products_page.click_add_product_1()
        self.checkout_process_page.click_payment_btn()
        self.checkout_process_page.click_checkout_btn()
        self.checkout_process_page.click_credit_card_btn()
        self.driver.switch_to.frame("yaadFrame")
        self.checkout_process_page.invalid_credit()
        text = self.checkout_process_page.error_message_card().get_attribute("innerText")
        assert text == "מספר כרטיס אשראי אינו תקין (418)"

