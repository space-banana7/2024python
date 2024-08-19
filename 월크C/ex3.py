import random
guess = 0 	
count = 0
answer= random.randint(1,100)
while guess!=answer:
    guess=int(input("숫자입력"))
    count=count+1
    
    if(guess>answer):
        print("DOWN")
    elif(guess<answer):	
        print("UP") 