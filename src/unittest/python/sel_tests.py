from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd
import unittest 
import random
import time 

class TestSelenium(unittest.TestCase): 
	
    def setUp(self): 
        self.data = pd.read_csv('csv_files//formID1.csv')
        self.data2 = pd.read_csv('csv_files//formID2.csv')
        self.data = self.data.set_index("labelName").T
        self.data2 = self.data2.set_index("labelName").T
        self.usr = {
            'email': '111@gmail.com',
            'name' : '111',
            'password' : 'pass#123'
        }
        self.driver =webdriver.Chrome()

    def test_all(self):
        self.driver.get("http://127.0.0.1:5000/") 
        # Login Button
        self.driver.implicitly_wait(5)
        time.sleep(2)

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
        time.sleep(2)
        element.click()
        self.driver.implicitly_wait(10)
        # User login
        element = self.driver.find_element_by_name('email')
        element.send_keys(self.usr['email'])
        element = self.driver.find_element_by_name('password')
        element.send_keys(self.usr['password'])
        element = self.driver.find_element_by_id('loginButton')
        time.sleep(2)
        element.click()
        self.driver.implicitly_wait(5)
        # Fill form
        
        for i in self.data:
            try:
                print(i)
                if self.data[i]['type'] == "radio":
                    try:
                        elID = self.data[i]['id']+'-'+str(random.randint(0,1))

                        element = self.driver.find_element_by_id(elID)
                        element.click()
                        pass
                    except:
                        print("error with:  ",i)
                        pass
                    
                elif self.data[i]['type'] == "dropdown":
                    element = Select(self.driver.find_element_by_id(self.data[i]['id']))
                    elText = random.choice(list(self.data[i][2:].dropna().unique().tolist()))
                    try:
                        element.select_by_visible_text(elText)
                        pass
                    except:
                        print("error with:  " + i, elText)
                        pass

                elif self.data[i]['type'] == "textbox":
                    try:
                        element = self.driver.find_element_by_id(self.data[i]['id'])
                        element.clear()
                        val = self.data[i]['value']
                        try:
                            val = int(val.strip())
                            val = random.randint(val//2,val)
                        except:
                            print('not integer', val)
                        element.send_keys(val)
                        pass
                    except:
                        print("error with:  ",i)
                        pass        
                
                else:
                    print("problem with ",i)
            except:
                print('error in:  ', i)

        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.driver.find_element_by_id('submit-button').click()
        self.driver.implicitly_wait(5)

        print("Starting form 2 checks")

        for i in self.data2:
            print(i)
            try:
                if self.data2[i]['type'] == "radio":
                    try:
                        elID = self.data2[i]['id']+'-'+str(random.randint(0,1))
                        element = self.driver.find_element_by_id(elID)
                        element.click()
                        pass
                    except:
                        print("error with:  ",i)
                        pass
                    
                elif self.data2[i]['type'] == "dropdown":
                    element = Select(self.driver.find_element_by_id(self.data2[i]['id']))
                    elText = random.choice(list(self.data2[i][2:].dropna().unique().tolist()))
                    try:
                        element.select_by_visible_text(elText)
                        pass
                    except:
                        print("error with:  " + i, elText)
                        pass

                elif self.data2[i]['type'] == "textbox":
                    try:
                        element = self.driver.find_element_by_id(self.data2[i]['id'])
                        element.clear()
                        val = self.data2[i]['value']
                        try:
                            val = int(val.strip())
                            val = random.randint(val//2,val)
                        except:
                            print('not integer', val)
                        element.send_keys(val)
                        pass
                    except:
                        print("error with:  ",i)
                        pass        
                
                else:
                    print("problem with ",i)

            except:
                print('error in:  ', i)

        self.driver.implicitly_wait(5)
        time.sleep(2)
        self.driver.find_element_by_id('submit-button').click()
        self.driver.implicitly_wait(5)
    
    def tearDown(self):
        print("tests ended")