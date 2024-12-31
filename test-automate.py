from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()  #browser initialization
from selenium.webdriver.common.keys import Keys

try:
    driver.get("http://10.0.16.206:5501/test.html")
    time.sleep(2)
    type_username=driver.find_element(By.ID,"username")#check data inside h1 tag
    type_username.send_keys("admin")
    time.sleep(2)
    type_password=driver.find_element(By.ID,"password")
    type_password.send_keys("12345")
    time.sleep(2)
    click_login=driver.find_element(By.ID,"login_button")
    click_login.click()
    time.sleep(2)
    # #system checks
    actualTitle=driver.title
    if actualTitle=="Dashboard":
        print("passed")
    else:
        print("failed")
    driver.back()
    time.sleep(6)
    type_username1=driver.find_element(By.ID,"username")#check data inside h1 tag
    type_username1.send_keys("admins")
    time.sleep(2)
    type_password1=driver.find_element(By.ID,"password")
    type_password1.send_keys("12345")
    time.sleep(2)
    click_login=driver.find_element(By.ID,"login_button")
    click_login.click()
    time.sleep(2)
    check_login=driver.find_element(By.ID,"error_message")
    print(check_login)
    if check_login.text=="Invalid username or password":
        print("passed")
    else:
        print("failed")
finally:
    driver.quit()
    