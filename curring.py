def curried_pow(x):
    def h(y):
        return pow(x, y)

    return h


def show_range(i, j, func):
    while i < j:
        print(func(i))
        i = i + 1


def curry2(f):
    """返回给定的双参数函数的柯里化版本"""

    def g(x):
        def h(y):
            return f(x, y)

        return h

    return g


def uncurry2(g):
    """返回给定的柯里化函数的双参数版本"""

    def f(x, y):
        return g(x)(y)

    return f


# print(curried_pow(2))#运行会报curring错误
# 下述两行结果完全相同
print(curried_pow(2)(3))
# 用c作为已经接收第一个参数的函数,则c运行时仅需一个参数,提高了函数重复利用性
c = curried_pow(2)
print(c(3))
show_range(0, 10, c)  # func仅接收一个参数,c符合要求,因此可以重复利用

pow_curried = curry2(pow)  # 自动柯里化
show_range(0, 10, pow_curried(2))
print(uncurry2(pow_curried)(2, 10))  # 逆柯里化
# uncurry2(pow_curried)即把柯里化的函数逆转,因此结果即pow(2,10)的结果
