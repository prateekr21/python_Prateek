from selenium import webdriver
from selenium.webdriver.common.by import By


driver =webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()



# driver.find_element(By.XPATH, "//input[@id='tuesday']").click()

# input("enter anything")


allcheck =driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")

print(len(allcheck))

for checkbox in allcheck:
    weekend=checkbox.get_attribute("id")
    if weekend=="saturday" or weekend=="sunday":
        checkbox.click()

input("enter anything")