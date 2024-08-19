import random
numbers=[]
result="my numbers:"
cnt=0
while cnt<6:
    num=random.randint(1,46)
    if num not in numbers:
        numbers.append(num)
        result=result+f" {num}"
        cnt+=1
print(result)