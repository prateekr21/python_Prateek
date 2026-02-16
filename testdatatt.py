from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import Xlutils
import time

driver = webdriver.Chrome()
driver.implicitly_wait(20)
driver.maximize_window()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true")

file="C:\\Users\\hpx\\Desktop\\VIN\\caldata.xlsx"

rows=Xlutils.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    Prc=Xlutils.readData(file,"Sheet1",r,1)
    RateOfInt=Xlutils.readData(file,"Sheet1",r,2)
    Period1=Xlutils.readData(file,"Sheet1",r,3) 
    Period2=Xlutils.readData(file,"Sheet1",r,4)
    frc=Xlutils.readData(file,"Sheet1",r,5)
    ExpectedR=MaturityVal= Xlutils.readData(file,"Sheet1",r,6)
        
    #Passing values to the application
    driver.find_element(By.ID,"principal").send_keys(Prc)
    driver.find_element(By.ID,"interest").send_keys(RateOfInt)
    driver.find_element(By.ID,"tenure").send_keys(Period1)  
    selct=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    selct.select_by_visible_text(Period2)

    select2=Select(driver.find_element(By.ID,"frequency"))
    select2.select_by_visible_text(frc)   
    
    actualR=driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

#Validation
if float(ExpectedR)==float(actualR):
    print("Test is passed")
    Xlutils.writeData(file,"Sheet1",r,8,"Passed")
    Xlutils.fillGreenColor(file,"Sheet1",r,8)
else:
    print("Test is failed")
    Xlutils.writeData(file,"Sheet1",r,8,"Failed")
    Xlutils.fillRedColor(file,"Sheet1",r,8)

driver.find_element(By.XPATH,"//img[@class='PL5']").click() #click on reset button
time.sleep(2)
