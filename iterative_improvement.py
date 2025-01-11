def improve(update, close, guess=1):  # updata()方法可以作为参数传入函数
    while not close(guess):  # guess为初始值
        guess = update(guess)  # 不断优化
    return guess


def golden_update(guess):  # 优化器:加上正数的倒数加上 1
    return 1 / guess + 1


def approx_eq(x, y, tolerance=1e-15):  # 极限误差
    return abs(x - y) < tolerance


def square_close_to_successor(guess):  # 比较器
    return approx_eq(guess * guess, guess + 1)


def sqrt(a):
    def average(a, b):
        return (a + b) / 2

    def sqrt_update(x):  # 优化器
        return average(x, a / x)

    def sqrt_close(x):  # 比较器
        return approx_eq(x * x, a)

    # 上述三个函数都仅在sqrt()函数中生效,体现了作用域的定义
    return improve(sqrt_update, sqrt_close)


if __name__ == "__main__":
    # print(improve(golden_update, square_close_to_successor))
    # 黄金比例的一个著名的特性是它可以通过反复叠加任何正数的倒数加上 1 来计算，而且它比它的平方小 1
    print(sqrt(256))
