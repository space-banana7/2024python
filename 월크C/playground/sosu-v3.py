# 소수 편차 그래프 그리기
from matplotlib import pyplot
import math
nanugi_record=[]
result_record=[]
chie_record=[0.0]
x=[]
num1=int(input("시작 숫자 : "))
auto=int(input("반복 횟수 : "))

for i in range(auto-1):
    x.append(i+1)

while auto!=0:
    num2=num1
    while num2>=1:
        if num1%num2==0:
            nanugi_record.append(num2)
        num2-=1
    if len(nanugi_record)==2:
        result_record.append(num1)
        auto-=1
    num1+=1
    nanugi_record=[]

for i in range(len(result_record)-2):
    chie_record.append((result_record[i+2]-result_record[i+1])/2)

print(result_record)
print(chie_record)
pyplot.plot(x,chie_record,color="blue")
pyplot.show()