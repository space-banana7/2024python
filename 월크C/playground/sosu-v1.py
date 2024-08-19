# 소수 나열하기
import time
record=[]
t=1
print("시작 숫자는?")
num1=int(input())
if num1<1:
    print("1 이상의 정수만 입력 가능")
while t==1:
    num2=num1
    while num2>=1:
        if num1%num2==0:
            record.append(num2)
        num2-=1
    if len(record)==2:
        print(num1)
    num1+=1
    record=[]
    time.sleep(0.01)