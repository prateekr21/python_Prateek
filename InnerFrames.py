from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.maximize_window()


driver.find_element(By.XPATH,"//*[@id='singleframe']")


