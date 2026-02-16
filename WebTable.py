from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()


driver.implicitly_wait(200)
driver.get("https://testautomationpractice.blogspot.com/")

# Count number of row and column
noOfRow =len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody//tr"))
noOfCol=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tbody//tr[1]//th"))

print(noOfRow)
print(noOfCol)

# Read specific row and column data
datatable=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[5]/td[1]").text
print(datatable)

# Read all row and column data
# for r in range(2,noOfRow+1):
#     for c in range(1,noOfCol+1):
#         datatable=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(datatable,end='                  ')

#     print()


# Read data based on conditions (list books name whose author is mukesh)

for r in range(2,noOfRow+1):
    Auth=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]")
    if Auth== "Mukesh":
        bookname=driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]")
        print(bookname,"          ",Auth)
        

