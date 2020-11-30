from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd
import unittest 

class TestSelenium(unittest.TestCase): 
	
    def setUp(self): 
        self.data = pd.read_csv('formID.csv')
        self.data = self.data.set_index("labelName").T
        self.driver = webdriver.Firefox(executable_path="./geckodriver") 
        self.driver.get("http://127.0.0.1:5000/") 

    def test_selenium(self):		 

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

        self.driver.find_element_by_id('submit-button').click()

    def tearDown(self):
                 
            print("tests ended")
            self.driver.quit()

if __name__ == '__main__': 
	unittest.main() 

