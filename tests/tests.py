from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd
import unittest 

class TestSelenium(unittest.TestCase): 
	
    def setUp(self): 
        self.data = pd.read_csv('../csv_files/formID.csv')
        self.data = self.data.set_index("labelName").T
        self.usr = {
            'email': '111@gmail.com',
            'name' : '111',
            'password' : 'pass#123'
        }
        self.driver = webdriver.Firefox(executable_path='./geckodriver')

    def test_all(self):
        self.driver.get("http://0.0.0.0:5000/") 
        # Login Button
        self.driver.implicitly_wait(5)

        element = self.driver.find_element_by_id('loginButton')
        element.click()
        
        self.driver.implicitly_wait(10)

        # Create user
        element = self.driver.find_element_by_id('signupNav')
        element.click()
        element = self.driver.find_element_by_name('email')
        element.send_keys(self.usr['email'])
        element = self.driver.find_element_by_name('name')
        element.send_keys(self.usr['name'])
        element = self.driver.find_element_by_name('password')
        element.send_keys(self.usr['password'])
        element = self.driver.find_element_by_id('signupButton')
        element.click()
        element = self.driver.find_element_by_id('loginNav')
        element.click()
        self.driver.implicitly_wait(10)
        # User login
        element = self.driver.find_element_by_name('email')
        element.send_keys(self.usr['email'])
        element = self.driver.find_element_by_name('password')
        element.send_keys(self.usr['password'])
        element = self.driver.find_element_by_id('loginButton')
        element.click()
        self.driver.implicitly_wait(5)
        # Fill form
        for i in self.data:
            if self.data[i]['type'] == "radio":
                element = self.driver.find_element_by_id(self.data[i]['id'])
                element.click()
                pass

            elif self.data[i]['type'] == "dropdown":
                element = Select(self.driver.find_element_by_id(self.data[i]['id']))
                element.select_by_visible_text(self.data[i]['value'])
                pass

            elif self.data[i]['type'] == "textbox":
                element = self.driver.find_element_by_id(self.data[i]['id'])
                element.clear()
                element.send_keys(self.data[i]['value'])
                pass

            else:
                print("problem with ",i)
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('submit-button').click()
        self.driver.implicitly_wait(5)


    # def login_button(self):
    #     self.driver.get("http://0.0.0.0:5000/") 
    #     element = self.driver.find_element_by_id('loginButton')
    #     element.click()

    # def test_create_user(self):
    #     self.driver.get("http://0.0.0.0:5000/login") 
    #     element = self.driver.find_element_by_id('signupNav')
    #     element.click()
    #     element = self.driver.find_element_by_name('email')
    #     element.send_keys(self.usr['email'])
    #     element = self.driver.find_element_by_name('name')
    #     element.send_keys(self.usr['name'])
    #     element = self.driver.find_element_by_name('password')
    #     element.send_keys(self.usr['password'])
    #     element = self.driver.find_element_by_id('signupButton')
    #     element.click()

    # def test_login_user(self):
    #     self.driver.get("http://0.0.0.0:5000/login") 
    #     element = self.driver.find_element_by_name('email')
    #     element.send_keys(self.usr['email'])
    #     element = self.driver.find_element_by_name('password')
    #     element.send_keys(self.usr['password'])
    #     element = self.driver.find_element_by_id('loginButton')
    #     element.click()

    # def test_selenium(self):		 
    #     self.drver.get("http://0.0.0.0:5000/profile") 
    #     element = self.driver.find_element_by_name('email')
    #     element.send_keys(self.usr['email'])
    #     element = self.driver.find_element_by_name('password')
    #     element.send_keys(self.usr['password'])
    #     element = self.driver.find_element_by_id('loginButton')
    #     element.click()
    #     for i in self.data:
    #         if self.data[i]['type'] == "radio":
    #             element = self.driver.find_element_by_id(self.data[i]['id'])
    #             element.click()
    #             pass

    #         elif self.data[i]['type'] == "dropdown":
    #             element = Select(self.driver.find_element_by_id(self.data[i]['id']))
    #             element.select_by_visible_text(self.data[i]['value'])
    #             pass

    #         elif self.data[i]['type'] == "textbox":
    #             element = self.driver.find_element_by_id(self.data[i]['id'])
    #             element.clear()
    #             element.send_keys(self.data[i]['value'])
    #             pass

    #         else:
    #             print("problem with ",i)

    #     self.driver.find_element_by_id('submit-button').click()

    def tearDown(self):
                 
            print("tests ended")
            # self.driver.quit()

if __name__ == '__main__': 
	unittest.main() 
