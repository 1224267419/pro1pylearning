from functools import reduce
from operator import mul
def count(s, value):
    """统计在序列 s 中出现了多少次值为 value 的元素"""
    total = 0
    for elem in s:
        if elem == value:
            total = total + 1
    return total


digits = [1, 2, 3] + [4, 5] * 3 + [8] * 2
print(digits)
print(count(digits, 8))

pairs = [[1, 2], [2, 2], [2, 3], [4, 4]]
same_count = 0
for x, y in pairs:  # 将 x 和 y 分别绑定到每对中的第一个元素和第二个元素
    if x == y:
        same_count = same_count + 1
print(same_count)

print(list(range(5, 8)))  # range用于创建一个从i到j-1的列表,隐含参数步长默认为1
print(list(range(4)))#range默认初始值为0
odds = [1, 3, 5, 7, 9]
print([x+1 for x in odds])#通过for对序列中的每个元素使用一个固定表达式进行计算，并将结果值保存在新序列中

print([x for x in odds if 25 % x == 0])


def product(s):
    return reduce(mul, s)

print(product([1, 2, 3, 4, 5]))
print(2 in [1,2,3,4,5])
