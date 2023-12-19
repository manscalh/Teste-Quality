from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import unittest
from time import sleep
from tests.users import Users
from tests.page import Page

class TestPassword(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.STANDARD_USER)
    
    def tearDown(self) -> None:
        self.driver.quit()
        
    def test_CT08_default_password(self):
       
        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.INVENTORY_TITLE,title)
        
        sleep(1)
        
    def test_CT09_empty_password(self):
        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA_EMPTY)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        message = self.driver.find_element(by=By.CLASS_NAME, value='error-message-container').text
        
        self.assertEqual(Page.LOGIN_PAGE_EMPTY_PASSWORD,message)
        
        sleep(1)
        
    def test_CT10_invalid_password(self):
        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA_INVALID)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        message = self.driver.find_element(by=By.CLASS_NAME, value='error-message-container').text
        
        self.assertEqual(Page.LOGIN_PAGE_INVALID_PASSWORD,message)
        
        sleep(1)
        
if __name__ == '__main__':
        unittest.main()