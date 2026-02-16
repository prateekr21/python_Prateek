from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(300)

DoubleClick=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
Act=ActionChains(driver)
Act.double_click(DoubleClick).perform()

input("Enter any")