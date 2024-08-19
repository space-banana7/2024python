def sum(*numbers):
    sum_value=0
    for numbers in numbers:
        sum_value=sum_value+numbers
    return sum_value

result=sum(1,3)
print(result)