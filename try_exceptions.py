def invert(x):
    result = 1 / x  # 抛出一个异常（ZeroDivisionError) 如果 x 为 0
    print('Never printed if x is 0')
    return result


def invert_safe(x):
    try:
        return invert(x)
        # 即使执行了1/0也不会有任何报错,因为使用try处理了异常
    except ZeroDivisionError as e:
        return str(e)


print(invert_safe(2))
print(invert_safe(0))
