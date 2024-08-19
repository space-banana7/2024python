# 피라미드 만들기
floar=int(input())
count=1
for i in range(floar):
    for g in range(floar-i):
        print(" ",end=" ")
    for g in range(count):
        print("M",end=" ")
    print(" ")
    count+=2