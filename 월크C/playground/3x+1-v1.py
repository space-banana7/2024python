# 콜라츠 추측 나열하기
print("시작 숫자는?")
t=0
num1=int(input())
num2=num1
if num1<1:
    print("1 이상의 정수만 입력 가능")
else:
    while t!=9999999999999999:
        while num2!=1:
            if num2%2==1:
                num2=num2*3+1
            num2/=2
        print(num1)
        num1+=1
        num2=num1
        t+=1