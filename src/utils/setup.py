


import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from src.pages.home_page import Homepage
from src.pages.footer_links_page import Footer_linkspage
from src.pages.search_page import Searchpage
from src.pages.products_page import Productspage
from src.pages.registration_page import Registrationpage
from src.pages.login_page import Loginpage
from src.pages.personal_area_page import Personal_areapage
from src.pages.checkout_process_page import Checkout_processpage

from selenium.webdriver.chrome.options import Options

class WebDriverSetup:

    @pytest.fixture()
    def setUp(self):
        chromedriver_path = "C:/Webdriver/chromedriver.exe"
        service = Service(executable_path=chromedriver_path)
        options = webdriver.ChromeOptions()
        options.add_argument("--disable-extensions")
        self.driver = webdriver.Chrome(service=service, options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(30)
        self.driver.get("https://qa.trado.co.il/")
        self.home_page = Homepage(self.driver)
        self.home_page.click_restaurants_and_save()
        self.footer_links_page = Footer_linkspage(self.driver)
        self.search_page = Searchpage(self.driver)
        self.products_page = Productspage(self.driver)
        self.registration_page = Registrationpage(self.driver)
        self.login_page = Loginpage(self.driver)
        self.personal_area_page = Personal_areapage(self.driver)
        self.checkout_process_page = Checkout_processpage(self.driver)
        yield self.driver
        self.driver.quit()

