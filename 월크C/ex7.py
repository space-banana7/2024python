import requests
from bs4 import BeautifulSoup
url="https://www.aladin.co.kr/home/welcome.aspx"
response=requests.get(url)
# print(response.text)
sans=BeautifulSoup(response.text,"html.parser")
result=sans.select('.sub')
# print(result)
for r in result:
    print(r.text)