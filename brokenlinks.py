import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.deadlinkcity.com/")

all_links = driver.find_elements(By.TAG_NAME, "a")

count = 0

for link in all_links:
    url = link.get_attribute("href")

    if not url:
        continue

    try:
        res = requests.head(url, timeout=5)

        if res.status_code >= 400:
            print(url, "Broken links")
            count += 1
        else:
            print(url, "Valid links")

    except:
        print(url, "Error links")
        count += 1

print("Total broken:", count)

driver.quit()
