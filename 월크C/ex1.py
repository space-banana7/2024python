import random
result='my_number:'
for i in [0,1,2]: #0~5까지 6번 반복실행
    num=random.randint(1,46)
    result=f"주사위숫자: {num}"
    print(result)