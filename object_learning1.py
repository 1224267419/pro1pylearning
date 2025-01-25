def demo():
    """这是一个测试函数"""
    print("这是测试函数")


class Person:
    def __init__(self, new_name="无名"):  # 通过默认参数从而使得部分参数可选
        self.name = new_name  # 用__init__来初始化类的属性

    def __str__(self):  #
        return "我是人"

    def eat(self):
        print("%s喜欢吃东西" % self.name)

    def __del__(self):  # 删除时执行
        print(self.name + "被删除")
        # return "11"


print(dir(demo()))
print(demo.__doc__)  # 输出了demo声明下一行的内容
xiaoming = Person("小明")
xiaoming2 = xiaoming  # 此时两个小明指向同一个对象(地址引用
# xiaoming.name = "xiaoming"
xiaoming.eat()
xiaohong = Person()
print(xiaohong)
