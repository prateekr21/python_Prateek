from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(200)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
windowID=driver.window_handles

parentwindowID = windowID[0]
childwindowID = windowID[1]


driver.switch_to.window(childwindowID)
print(driver.title)

driver.switch_to.window(parentwindowID)
print(driver.title)





