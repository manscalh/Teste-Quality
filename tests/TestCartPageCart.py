from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import unittest
from time import sleep
from tests.users import Users
from tests.page import Page

class TestCartPageCart(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
                
        sleep(0.5)
        
        text_user = self.driver.find_element(by=By.XPATH, value="//form//input[@id='user-name']")
        text_user.send_keys(Users.ERROR_USER)
        
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
        
    def tearDown(self) -> None:
        self.driver.quit() 
        
    def test_CT22_remove_cart_error_user(self):
          
        xpath = '//div[contains(text(),"'+Page.CART_ADD_REMOVE_SAUCE_LABS_BACKPACK_TEXT+'")]/../../..//*/div[@class="inventory_item_price" and text()[2]="'+Page.CART_ADD_REMOVE_SAUCE_LABS_BACKPACK_PRICE+'"]/../button'

        card = self.driver.find_element(by=By.XPATH, value=xpath)
        card.click()
        
        sleep(0.5)
        
        xpath = "//*[@class='shopping_cart_link']"
        cart_qtd = self.driver.find_element(by=By.XPATH, value=xpath).text
        
        sleep(0.5)
        
        self.assertEqual(Page.CART_EMPTY_QTD,cart_qtd)      

if __name__ == '__main__':
        unittest.main()