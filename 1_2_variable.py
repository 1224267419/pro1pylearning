from math import pi
from math import sqrt

print(sqrt(29))
print("%.2f" % pi)
a, b = 10, 20  # py允许一行对多个变量赋值
print(print(1), print(2))


def g():
    return 1


print(g())
g = 2
print(g)


# print(g())#此时g已经是值而非函数
def pressure(v, t, n):
    """计算理想气体的压力，单位为帕斯卡

    使用理想气体定律：http://en.wikipedia.org/wiki/Ideal_gas_law

    v -- 气体体积，单位为立方米
    t -- 绝对温度，单位为开尔文
    n -- 气体粒子
    """
    k = 1.38e-23  # 玻尔兹曼常数
    return n * k * t / v


print(help(pressure))  # 输出文档字符串(紧跟在定义式后的'''注释
def fib(k):
    i, j = 0, 1
    while k >0:
        # print(j)
        i, j = j, i + j
        k = k - 1
    return j
print(fib(9))
assert fib(9)==55