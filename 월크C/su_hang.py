from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def blind_sun():
    driver=webdriver.Chrome()
    driver.get("https://astro.kasi.re.kr/learning/pageView/6233")
    driver.implicitly_wait(0.5)
    search=driver.find_element(by=By.CSS_SELECTOR,value=".cont.w25")
    print(search.text)

def blind_moon():
    driver=webdriver.Chrome()
    driver.get("https://astro.kasi.re.kr/learning/pageView/5934")
    driver.implicitly_wait(0.5)
    search=driver.find_element(by=By.CSS_SELECTOR,value=".cont.w25")
    print(search.text)
    driver.close()
    kind=input("어떤거?\n년월일 숫자로만 입력\n")
    driver=webdriver.Chrome()
    driver.implicitly_wait(0.5)
    driver.get(f"https://astro.kasi.re.kr/resources/images/lunareclipse_2023/LE_Diagram_{kind}.png")
    time.sleep(100)
        

want=input("일식 또는 월식\n")
if want=="일식":
    blind_sun()
elif want=="월식":
    blind_moon()
else:
    print("잘못된 입력으로 프로그램을 종료합니다.")