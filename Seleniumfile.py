# Python program to demonstrate 
# selenium 
# selenium script
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd

data = pd.read_csv('formID.csv')
data = data.set_index("labelName").T

driver = webdriver.Firefox(executable_path="./geckodriver") 
driver.get("http://127.0.0.1:5000/") 
print(data)

for i in data:
    if data[i]['type'] == "radio":
        element = driver.find_element_by_id(data[i]['id'])
        element.click()
        pass

    elif data[i]['type'] == "dropdown":
        element = Select(driver.find_element_by_id(data[i]['id']))
        element.select_by_visible_text(data[i]['value'])
        pass

    elif data[i]['type'] == "textbox":
        element = driver.find_element_by_id(data[i]['id'])
        element.clear()
        element.send_keys(data[i]['value'])
        pass

    else:
        print("problem with ",i)
driver.find_element_by_id('submit-button').click()
print("exit")

