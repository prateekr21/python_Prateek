from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
driver.implicitly_wait(300)


Min_slider=driver.find_element(By.XPATH,"(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
Max_slider=driver.find_element(By.XPATH,"(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")

print("Location of slider before moving...........")

print(Min_slider.location)  #{'x': 927, 'y': 2027}
print(Max_slider.location)  #{'x': 1057, 'y': 2027}

Act=ActionChains(driver)

Act.drag_and_drop_by_offset(Min_slider,900,0).perform()
Act.drag_and_drop_by_offset(Max_slider,-37,0).perform()

print("Location of slider After moving...........")

print(Min_slider.location) 
print(Max_slider.location) 