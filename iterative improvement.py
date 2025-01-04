def improve(update, close, guess=1):  # updata()方法可以作为参数传入函数
    while not close(guess):
        guess = update(guess)  # 不断优化
    return guess


def golden_update(guess):#优化器:加上正数的倒数加上 1
    return 1 / guess + 1


def approx_eq(x, y, tolerance=1e-15):
    return abs(x - y) < tolerance


def square_close_to_successor(guess):#比较器
    return approx_eq(guess * guess, guess + 1)


if __name__ == "__main__":
    print(improve(golden_update, square_close_to_successor))
    # 黄金比例的一个著名的特性是它可以通过反复叠加任何正数的倒数加上 1 来计算，而且它比它的平方小 1
