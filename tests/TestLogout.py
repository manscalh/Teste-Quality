from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

import unittest
from time import sleep
from tests.users import Users
from tests.page import Page

class TestLogout(unittest.TestCase):
    
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
        
    def test_CT11_logout(self):
       
        sleep(1)
        option_menu = self.driver.find_element(by=By.ID, value='react-burger-menu-btn')
        option_menu.click()
        
        sleep(1)

        option_logout = self.driver.find_element(by=By.ID, value='logout_sidebar_link')
        option_logout.click()
        
        sleep(1)
        
        field_Password_for_all_users = self.driver.find_element(by=By.CLASS_NAME,value="login_password").text
        self.assertEqual(Page.MAIN_PAGE_PASSWORD_ALL_USERS,field_Password_for_all_users)
        
        
if __name__ == '__main__':
        unittest.main()