from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://text-compare.com/")
driver.implicitly_wait(300)

int1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
int2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")

int1.send_keys("WellCometogg")

Act=ActionChains(driver)

#input ctrl+A Select Text
Act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
#input ctrl +C copy text
Act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
#input Tab 
Act.key_down(Keys.TAB).key_up(Keys.TAB).perform()
#input Ctrl + V
Act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

input(".........enter.......")