import random
def star(maga,re):
    for r in range(1,re+1):
        n=random.randint(1,maga)
        print(r,"결과",n)
star(10,5)