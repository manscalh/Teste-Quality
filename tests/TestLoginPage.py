from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import unittest
from time import sleep
from tests.users import Users
from tests.page import Page

class TestLoginPage(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) 
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
    
    def tearDown(self) -> None:
        self.driver.quit()
        
    def test_CT01_standard_user_login(self):
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.STANDARD_USER)

        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.INVENTORY_TITLE,title)
        
        sleep(2)
        
    def test_CT02_locked_out_user_login(self):
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.LOCKED_OUT_USER)

        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        message = self.driver.find_element(by=By.CLASS_NAME, value='error-message-container').text
        
        self.assertEqual(Page.LOGIN_PAGE_MESSAGE_BLOCKED_USER,message)
        
        sleep(2)
        
    def test_CT03_empty_login(self):
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys("")
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        message = self.driver.find_element(by=By.CLASS_NAME, value='error-message-container').text
        
        self.assertEqual(Page.LOGIN_PAGE_EMPTY_USER,message)
        
        sleep(2)
        
    def test_CT04_problem_user_Login(self):
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.PROBLEM_USER)
        
        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        
        self.assertEqual(Page.INVENTORY_TITLE,title)
        
        sleep(2)
        
    def test_CT05_performance_glitch_user_login(self):
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.PERFORMANCE_GLITCH_USER)

        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.INVENTORY_TITLE,title)
        
        sleep(2)
        
    def test_CT06_error_user_login(self):
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.ERROR_USER)

        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.INVENTORY_TITLE,title)
        
        sleep(2)
        
    def test_CT07_visual_user_login(self):
        text_user = self.driver.find_element(by=By.ID, value='user-name')
        text_user.send_keys(Users.VISUAL_USER)

        text_password = self.driver.find_element(by=By.ID, value='password')
        text_password.send_keys(Users.SENHA)
        
        sleep(1)

        button_login = self.driver.find_element(by=By.ID, value='login-button')
        button_login.click()
        
        title = self.driver.find_element(by=By.CLASS_NAME,value="title").text
        self.assertEqual(Page.INVENTORY_TITLE,title)
        
        sleep(2)


if __name__ == '__main__':
        unittest.main()