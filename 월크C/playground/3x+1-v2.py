# 숫자 하나로 콜라츠 추측
print("숫자는?")
num1=float(input())
if num1<1:
    print("1 이상의 정수만 입력 가능")
else:
    while num1!=1:
        if num1%2==1:
            num1=num1*3+1
            print(num1)
        num1/=2.0
        print(num1)