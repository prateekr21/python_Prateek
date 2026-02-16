from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

driver =webdriver.Chrome()

driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()
driver.save_screenshot("C:\\Users\\hpx\\Desktop\\New folder\\homepage.png")
driver.save_screenshot(os.getcwd()+"\\again.png")

driver.get_screenshot_as_file(os.getcwd()+"\\hh.png")

driver.get_screenshot_as_png()  #driver.get_screenshot_as_base64 saves in binary formate
driver.quit()
