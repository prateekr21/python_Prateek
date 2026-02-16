from selenium import webdriver
import time
from selenium.webdriver.common.by import By

ops= webdriver.ChromeOptions()
ops.add_argument("--disable-notification")
driver=webdriver.Chrome()



driver.get("https://whatmylocation.com/")
driver.maximize_window()

