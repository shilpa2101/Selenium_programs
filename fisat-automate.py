from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()  #browser initialization
from selenium.webdriver.common.keys import Keys

try:
    driver.get("https://fisat.ac.in/")
    time.sleep(2)
    check_academics=driver.find_element(By.ID,"menu-item-dropdown-4054")#check data inside h1 tag
    check_academics.click()
    time.sleep(2)
    check_dept=driver.find_element(By.ID,"menu-item-dropdown-4059")
    check_dept.click()
    time.sleep(2)
    check_computer_application=driver.find_element(By.ID,"menu-item-dropdown-4144")
    check_computer_application.click()
    time.sleep(2)
    #system checks
    actualTitle=driver.title
    if actualTitle=="Computer Applications | FISAT | Federal Institute of Science And Technology":
        print("passed")
    else:
        print("failed")
finally:
    driver.quit()