class Dog:
    long = 100  # 类属性
    __eat = 19  # 食量

    def change_long(self, l):
        self.long = l

    @classmethod  # 类方法修饰符
    def info_eat(cls):
        return cls.__eat

    @staticmethod
    def pri_who_am_i():#无需self或者cls参数,减少性能损耗
        print("我是狗类")
print(Dog.long)
dog = Dog()  # 实例化
dog.long = 20
print(dog.long)  # 对象只会修改自己的属性,不能修改类属性
print(Dog.long)
Dog.long = 50  # 要直接修改类属性
print(Dog.long)
# print(Dog.__eat)#不能直接访问
print(Dog.info_eat())  # 类本身通过类方法访问私有类属性
print(dog.info_eat())  # 对象也可以通过类方法访问私有类属性
Dog.pri_who_am_i()