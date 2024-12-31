from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()  #browser initialization
from selenium.webdriver.common.keys import Keys

try:
    driver.get("https://www.amazon.in")
    time.sleep(5)
    check_element=driver.find_element(By.ID,"twotabsearchtextbox")#check data inside h1 tag
    check_element.send_keys("iphone 16")
    time.sleep(5)
    check_element.send_keys(Keys.ENTER)
    time.sleep(2)
    print("passed")
finally:
    driver.quit()