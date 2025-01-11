import iterative_improvement


def newton_update(f, df):  # f为映射函数,df为f的导数
    def updata(x):
        return x - f(x) / df(x)

    return updata  # 优化函数


def find_zero(f, df):
    def near_zero(x):  # 拟合条件
        return iterative_improvement.approx_eq(f(x), 0)  # f=0?

    return iterative_improvement.improve(newton_update(f, df), near_zero)


def square_root_newton(a):  # 这是已知f和df的情况
    def f(x):
        return x * x * x - a

    def df(x):
        return 3 * x * x

    return find_zero(f, df)


def nth_root_of_a(a, n):#对于x^n=a
    def f(x):
        return x ** n-a

    def df(x):
        return n * (x ** (n - 1))

    return find_zero(f, df)


# print(square_root_newton(64))
print(nth_root_of_a(64, 2))
print(nth_root_of_a(64, 3))
