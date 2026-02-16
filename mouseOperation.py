from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(300)

#mouseHover
over=driver.find_element(By.XPATH,"//button[@class='dropbtn']")
Act=ActionChains(driver)
Act.move_to_element(over).perform()
time.sleep(30)



