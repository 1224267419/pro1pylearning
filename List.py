chinese = ['coin', 'string', 'myriad']
suit = chinese  # 别名
suit2 = list(chinese)
print(chinese.pop())
print(suit)  # 弹出后仅剩两个元素
suit.extend(['sword', 'club'])  # 在末尾增加元素
print(suit)
print(suit2)  # 用list构造器,使得suit2不绑定在chinese上
print(suit is ['coin', 'string', 'sword', 'club'])  # py用is检测两个变量是否指向同一目标


def pingfang(a):
    return a * a


a = [-1, 2, 3, 4, 5, 6, 7, -8, 1]
print(min(a, key=abs))  # 通过高级函数传递key方法,找出在key函数条件下返回值最小的值
b = list(map(pingfang, a))
print(b)
"""
对于上述列表a,我们可以通过下述方法找出函数返回的最小值
再通过迭代找出最小值所在索引号
"""
min_abs = abs(min(a, key=abs))
print(min_abs)
print([x for x in a if abs(x) == min_abs])  # 输出绝对值最小的元素
print([x for x in range(len(a)) if abs(a[x]) == min_abs])  # 找出最小值所在索引
