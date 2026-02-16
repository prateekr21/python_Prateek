from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver =webdriver.Chrome()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.implicitly_wait(20)

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
driver.find_element(By.XPATH,"//select[@id='billing_country']")
