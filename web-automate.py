from selenium import webdriver
from selenium.webdriver.common.by import By  #search tag
import time
driver=webdriver.Chrome()  #browser initialization

try:
    driver.get("http://127.0.0.1:5500/index.html")  #website open
    time.sleep(5) #continue current stage for 5 sec
    check_element=driver.find_element(By.TAG_NAME,"h1")#check data inside h1 tag
    if check_element.text.strip()=="FISAT":
        nameTextbox=driver.find_element(By.NAME,"fname")
        nameTextbox.send_keys("shilpa")
        time.sleep(5)
        print("passed")
    else:
        print("failed")
finally:    
    driver.quit()