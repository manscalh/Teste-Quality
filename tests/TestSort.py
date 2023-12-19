from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import unittest
from time import sleep
from tests.users import Users
from tests.page import Page

class TestSort(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.STANDARD_USER)
        
        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        sleep(1)
    
    def tearDown(self) -> None:
        self.driver.quit()
        
    def test_CT12_Sort_Z_to_A(self):
        option_menu = self.driver.find_element(by=By.CLASS_NAME, value='product_sort_container')
        option_menu.click()
        
        sleep(0.5)

        option_menu.send_keys(Page.SORT_Z_TO_A)
        option_menu.click()
        
        sleep(1)
        
        text_selected = self.driver.find_element(by=By.CLASS_NAME, value='active_option').text
        self.assertEqual(Page.SORT_Z_TO_A,text_selected)
    
    def test_CT13_Sort_A_to_Z(self):
        option_menu = self.driver.find_element(by=By.CLASS_NAME, value='product_sort_container')
        option_menu.click()
        
        sleep(0.5)

        option_menu.send_keys(Page.SORT_A_TO_Z)
        option_menu.click()
        
        sleep(1)
        
        text_selected = self.driver.find_element(by=By.CLASS_NAME, value='active_option').text
        self.assertEqual(Page.SORT_A_TO_Z,text_selected)
        
    def test_CT14_sort_price_low_to_high(self):
        option_menu = self.driver.find_element(by=By.CLASS_NAME, value='product_sort_container')
        option_menu.click()
        
        sleep(0.5)

        option_menu.send_keys(Page.SORT_PRICE_LOW_TO_HIGH)
        option_menu.click()
        
        sleep(1)
        
        text_selected = self.driver.find_element(by=By.CLASS_NAME, value='active_option').text
        self.assertEqual(Page.SORT_PRICE_LOW_TO_HIGH,text_selected)
        
    def test_CT15_sort_price_high_to_low(self):
        option_menu = self.driver.find_element(by=By.CLASS_NAME, value='product_sort_container')
        option_menu.click()
        
        sleep(0.5)

        option_menu.send_keys(Page.SORT_PRICE_HIGH_TO_LOW)
        option_menu.click()
        
        sleep(1)
        
        text_selected = self.driver.find_element(by=By.CLASS_NAME, value='active_option').text
        self.assertEqual(Page.SORT_PRICE_HIGH_TO_LOW,text_selected)
       
        
if __name__ == '__main__':
        unittest.main()