from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os

driver =webdriver.Chrome()

driver.get("https://www.nopcommerce.com/en")
driver.maximize_window()
 
#capture all cookies from browser
cookies=driver.get_cookies()
print("print cookies:",len(cookies))

#Print details of all cookies
# for i in cookies:
#         print(i)
#         print(i.get('name'),":",i.get('value'))

#Add new cookie to the browser
driver.add_cookie({"name":"myCookie","value":"12345"})
driver.add_cookie({"name":"myCookieuii","value":"12887345"})
cookies=driver.get_cookies()
print("Size of the cookies",len(cookies))


#delet all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print("Size of the cookies",len(cookies))