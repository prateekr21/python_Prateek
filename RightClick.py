from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.implicitly_wait(300)


buton=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
Act=ActionChains(driver)
Act.context_click(buton).perform()

input("ehh")
