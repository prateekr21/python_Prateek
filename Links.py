from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/")

driver.maximize_window()


# clickonlink

# driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Jew").click()

leng= driver.find_elements(By.TAG_NAME, "a")
print(len(leng))

# print all the links
for link in leng:
    print(link.text)
    
input("enter anything")

