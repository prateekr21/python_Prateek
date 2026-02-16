from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import os
location=os.getcwd

def Chrome_setUp():
    preferences={"download.default_directory":location}
  
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)

    driver= webdriver.Chrome(options=ops)
    return driver


driver= Chrome_setUp()
driver.get("https://file-examples.com/index.php/sample-documents-download/")

driver.maximize_window()
driver.find_element(By.XPATH,"//a[@href='https://file-examples.com/index.php/sample-documents-download/sample-doc-download/']").click()