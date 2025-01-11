def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


l = [1, 2, 3, 4]
print(calc(1, 2))  # 1*1+2*2=5
print(calc(1, 2, 3, 4))
print(calc(*l))#*l即拆包,作为可变参数带回
