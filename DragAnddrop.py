from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(300)

drag=driver.find_element(By.ID,"draggable")
drop=driver.find_element(By.ID,"droppable")  

Act=ActionChains(driver)
Act.drag_and_drop(drag,drop).perform()

input("enter anything...")