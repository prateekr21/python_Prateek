from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")


#open alertwindow

driver.find_element(By.XPATH,"//button[@id='promptBtn']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("hellocdcdvd")
alertwindow.accept() #close alert clicking okey


