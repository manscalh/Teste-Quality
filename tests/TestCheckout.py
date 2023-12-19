from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import unittest
from time import sleep
from tests.users import Users
from tests.page import Page

class TestCheckout(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
                
        sleep(0.5)
        
        text_user = self.driver.find_element(by=By.XPATH, value="//form//input[@id='user-name']")
        text_user.send_keys(Users.STANDARD_USER)
        
        text_password = self.driver.find_element(by=By.XPATH, value="//form//input[@id='password']")
        text_password.send_keys(Users.SENHA)
        
        button_login = self.driver.find_element(by=By.XPATH, value="//form//input[@id='login-button']")
        button_login.click()
                
        sleep(0.5)

        xpath = '//div[contains(text(),"'+Page.CART_ADD_REMOVE_SAUCE_LABS_BACKPACK_TEXT+'")]/../../..//*/div[@class="inventory_item_price" and text()[2]="'+Page.CART_ADD_REMOVE_SAUCE_LABS_BACKPACK_PRICE+'"]/../button'

        card = self.driver.find_element(by=By.XPATH, value=xpath)
        card.click()
        
        sleep(0.5)
        
        xpath = "//*[@class='shopping_cart_link']"
        cart = self.driver.find_element(by=By.XPATH, value=xpath)
        cart.click()
        
        sleep(0.5)
        
        xpath = "//button[@id='checkout']"
        checkout = self.driver.find_element(by=By.XPATH, value=xpath)
        checkout.click()
        
    def tearDown(self) -> None:
        self.driver.quit() 
        
    def test_CT24_checkout_firtname_empty_standard_user(self):
        
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_EMPTY)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        xpath = "//H3[@data-test='error']"
        message = self.driver.find_element(by=By.XPATH,value=xpath).text
        self.assertEqual(Page.CHECKOUT_FIRTNAME_REQUERID,message)
        
        sleep(0.5)
        
    def test_CT25_checkout_lastname_empty_standard_user(self):
        
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_TEXT)
        
        xpath = "//input[@id='last-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_LASTNAME_EMPTY)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        xpath = "//H3[@data-test='error']"
        message = self.driver.find_element(by=By.XPATH,value=xpath).text
        self.assertEqual(Page.CHECKOUT_LASTNAME_REQUERID,message)
        
        sleep(0.5)
        
    def test_CT26_checkout_zipcode_empty_standard_user(self):
        
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_TEXT)
        
        xpath = "//input[@id='last-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_LASTNAME_TEXT)
        
        xpath = "//input[@id='postal-code']"
        zipcode = self.driver.find_element(by=By.XPATH, value=xpath)
        zipcode.send_keys(Page.CHECKOUT_ZIPCODE_EMPTY)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        xpath = "//H3[@data-test='error']"
        message = self.driver.find_element(by=By.XPATH,value=xpath).text
        self.assertEqual(Page.CHECKOUT_ZIPCODE_REQUERID,message)
        
        sleep(0.5)

    def test_CT27_checkout_firtname_standard_user(self):
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_TEXT)
        
        xpath = "//input[@id='last-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_LASTNAME_TEXT)
        
        xpath = "//input[@id='postal-code']"
        zipcode = self.driver.find_element(by=By.XPATH, value=xpath)
        zipcode.send_keys(Page.CHECKOUT_ZIPCODE_TEXT)
        
        sleep(0.5)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.CHECKOUT_PAGE_OVERVIEW,title)
        
        sleep(0.5)

    def test_CT28_checkout_lastname_standard_user(self):
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_TEXT)
        
        xpath = "//input[@id='last-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_LASTNAME_TEXT)
        
        xpath = "//input[@id='postal-code']"
        zipcode = self.driver.find_element(by=By.XPATH, value=xpath)
        zipcode.send_keys(Page.CHECKOUT_ZIPCODE_TEXT)
        
        sleep(0.5)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.CHECKOUT_PAGE_OVERVIEW,title)
        
        sleep(0.5)

    def test_CT29_checkout_zipcode_standard_user(self):
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_TEXT)
        
        xpath = "//input[@id='last-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_LASTNAME_TEXT)
        
        xpath = "//input[@id='postal-code']"
        zipcode = self.driver.find_element(by=By.XPATH, value=xpath)
        zipcode.send_keys(Page.CHECKOUT_ZIPCODE_TEXT)
        
        sleep(0.5)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.CHECKOUT_PAGE_OVERVIEW,title)
        
        sleep(0.5)
        
    def test_CT30_checkout_cancel_standard_user(self):
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_TEXT)
        
        xpath = "//input[@id='last-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_LASTNAME_TEXT)
        
        xpath = "//input[@id='postal-code']"
        zipcode = self.driver.find_element(by=By.XPATH, value=xpath)
        zipcode.send_keys(Page.CHECKOUT_ZIPCODE_TEXT)
        
        sleep(0.5)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        xpath = "//*[@id='cancel']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.INVENTORY_TITLE,title)
        
        sleep(0.5)

    def test_CT31_checkout_finish_standard_user(self):
        xpath = "//input[@id='first-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_FIRTNAME_TEXT)
        
        xpath = "//input[@id='last-name']"
        firt_name = self.driver.find_element(by=By.XPATH, value=xpath)
        firt_name.send_keys(Page.CHECKOUT_LASTNAME_TEXT)
        
        xpath = "//input[@id='postal-code']"
        zipcode = self.driver.find_element(by=By.XPATH, value=xpath)
        zipcode.send_keys(Page.CHECKOUT_ZIPCODE_TEXT)
        
        sleep(0.5)
        
        xpath = "//*[@id='continue']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        xpath = "//*[@id='finish']"
        btn_continue = self.driver.find_element(By.XPATH, xpath)
        btn_continue.click()
        
        sleep(0.5)
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.CHECKOUT_PAGE_COMPLETE,title)
        
        sleep(0.5)

if __name__ == '__main__':
        unittest.main()