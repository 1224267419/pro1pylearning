def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance  # 通过nonlocal使得函数可以修改自己栈帧以外的数据
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance

    return withdraw


def make_withdraw2(balance):
    def withdraw(amount):
        balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance

    return withdraw


wd = make_withdraw(20)
wd2 = make_withdraw(5)
wd3 = wd
print(wd(5))
print(wd(3))
print(wd(13))  # withdraw过多
# wd2=make_withdraw2(20)
# print(wd2(5))#运行不了
print(wd2(3))  # 不同函数维护不同的balance
print(wd3(1))  # wd3和wd实际上指向同一栈帧
