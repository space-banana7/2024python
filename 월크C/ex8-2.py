from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get("https://www.naver.com")
driver.implicitly_wait(0.5)
query_text=f"현재 시간"
search=driver.find_element(by=By.CSS_SELECTOR,value="#query")
search.send_keys(query_text)
driver.implicitly_wait(0.5)
button=driver.find_element(by=By.ID,value="search-btn")
button.click()

dhseh=driver.find_element(by=By.CSS_SELECTOR,value=".time_hour")
print(dhseh.text,end="시 ")
dhseh=driver.find_element(by=By.CSS_SELECTOR,value=".time_minute")
print(dhseh.text,end="분 ")
dhseh=driver.find_element(by=By.CSS_SELECTOR,value=".time_second")
print(dhseh.text,end="초 ")
print("\n20301강지훈")
time.sleep(10)