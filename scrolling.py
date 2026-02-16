from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver= webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.implicitly_wait(300)

#1.Scrolling down page by pixel
driver.execute_script("window.scrollBy(0,300)","")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:",value)

#2.Scroll down page till the element is visible 
flag=driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:",value)

#3.scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:",value)
time.sleep(5)


#4.Scroll up in up page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number of pixel moved:",value)
