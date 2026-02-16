from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://support.hp.com/in-en")    

driver.implicitly_wait(300)

print(driver.title)
print(driver.current_url)
print(driver.page_source)