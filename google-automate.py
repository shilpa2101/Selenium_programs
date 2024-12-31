from selenium import webdriver
from  selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()  #browser initialization
from selenium.webdriver.common.keys import Keys

try:
    driver.get("https://www.google.com/")
    time.sleep(5)
    check_element=driver.find_element(By.NAME,"q")#check data inside h1 tag
    check_element.send_keys("fisat")
    time.sleep(5)
    check_element.send_keys(Keys.ENTER)
    time.sleep(2)
    print("passed")
finally:
    driver.quit()