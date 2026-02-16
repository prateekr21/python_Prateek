from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

dropdo=driver.find_element(By.XPATH, "//select[@id='country']")
drpcont=Select(dropdo)

#select option from the dropdown
# drpcont.select_by_visible_text("India")
# drpcont.select_by_value("canada")
# drpcont.select_by_index(5)


#caputre all value and print 
all_options=drpcont.options
print("Total no of list in dropdown",len(all_options))

for listt in all_options:
    print(listt.text)

#select option from dropdwonwithout using build-in method

for ops in all_options:
    if ops.text=="India":
        ops.click() 

input("enter any ....")