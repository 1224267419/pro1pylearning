def demo():
    """这是一个测试函数"""
    print("这是测试函数")


class Person:

    def eat(self):
        print()


print(dir(demo()))
print(demo.__doc__)  # 输出了demo声明下一行的内容
xiaoming = Person()
xiaoming2 = xiaoming  # 此时两个小明指向同一个对象(地址引用

xiaohong = Person
