# 소수 나열 그래프 그리기
from matplotlib import pyplot
record=[]
y=[]
t=1
num1=int(input("시작 숫자 : "))
repeat=int(input("반복 횟수 : "))
repeat2=int(repeat**2)
if num1<1 or repeat<1:
    print("1 이상의 정수만 입력 가능")
while t<=repeat:
    num2=num1
    while num2>=1:
        if num1%num2==0:
            record.append(num2)
        num2-=1
    if len(record)==2:
        y.append(num1)
        t=t+1
    num1+=1
    record=[]
x=range(repeat)
x_st=[]
for i in x:
    x_st.append(i*5)
# x2=[]
# for i in x:
#     x2.append((i**2)/30)
pyplot.scatter(x,y,color="blue")
pyplot.plot(x,x,color="gray")
pyplot.plot(x,x_st,color="gray")
# pyplot.plot(x,x2,color="black")
pyplot.show()