from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import keyboard
driver=webdriver.Chrome()
driver.get("https://time.navyism.com/?host=naver.com")
driver.implicitly_wait(0.5)
while True:
    sans=driver.find_element(by=By.ID,value="time_area")
    print(sans.text)
    if keyboard.read_key("a"):
        break
time.sleep(10)