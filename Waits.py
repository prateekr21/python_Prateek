from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException
)
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://support.hp.com/in-en")    
driver.maximize_window()


driver.implicitly_wait(300) 
myWait = WebDriverWait(
    driver,
    10,
    poll_frequency=2,
    ignored_exceptions=[
        NoSuchElementException,
        ElementNotVisibleException,
        ElementNotSelectableException
    ]
)



button=myWait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='wpr-signin-tablet']//p[contains(text(),'Sign in')]")))
button.click()


input("enter anything")