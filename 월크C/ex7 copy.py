import requests
from bs4 import BeautifulSoup
day=int(input())
if day>29:
    exit(0)
url=f"https://school.use.go.kr/eonyang-h/M01030601/list?ymd=202403{day}"
response=requests.get(url)
# print(response.text)
sans=BeautifulSoup(response.text,"html.parser")
result=sans.find('a',href=f"/eonyang-h/M01030601/list?ymd=202403{day}")
# print(result)
print(result.text)
print("20301강지훈")