import requests
from bs4 import BeautifulSoup
url="https://time.navyism.com/?host=https%3A%2F%2Fwww.aladin.co.kr%2Fhome%2Fwelcome.aspx"
response=requests.get(url)
sans=BeautifulSoup(response.text,"html.parser")
result=sans.find('div',onclick="dayNameControl()")
print(result)