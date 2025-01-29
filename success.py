class Father:  # 父类
    def __init__(self):
        self.name = "father"

    def __str__(self):
        return (self.name)


class Son(Father):  # 子类
    def __str__(self):  # 继承父类的name属性,重写Father的__str__方法
        return (self.name + "的儿子son")


class Master:
    def __init__(self):
        self.kongfu = "古法编程"
        self.__money = 100000

    def make_program(self):
        print(f'运用{self.kongfu}写代码')

    def getMoney(self):
        return self.__money
    def set_money(self,a):
        self.__money=a

class School:
    def __init__(self):
        self.kongfu = "培训班编程"

    def make_program(self):
        print(f'运用{self.kongfu}写代码')


class Student(Master, School):  # 多继承优先继承最左边的类的属性和方法
    def __init__(self):
        super().__init__()
        self.kongfu = "自己编程"

    def make_program(self):
        self.__init__()  # 若不调用自己的初始化,self.kongfu的属性值是上一次调用的init的值,可以注释这行交换调用方法顺序
        print(f'运用{self.kongfu}写代码')

    def make_program_school(self):
        School.__init__(self)  # 若无School类的初始化,会直接使用了最左侧父类定义的make_program()方法,不是想要的结果
        School.make_program(self)

    def make_program_master(self):
        Master.__init__(self)
        Master.make_program(self)

    def make_program_old_1(self):  # 能实现功能,但太过累赘
        School.__init__(self)  # 若无School类的初始化,会直接使用了最左侧父类定义的make_program()方法,不是想要的结果
        School.make_program(self)
        Master.__init__(self)
        Master.make_program(self)
        # 写法1: 下面两行为super带参数的和上式等价
        # super(School, self).__init__()
        # super(School, self).make_program()
        # 写法2:仅调用上一级的父类方法
        super().__init__()
        super().make_program()


class Sun(Student):
    pass


if __name__ == '__main__':
    father = Father()
    son = Son()
    print(father)
    print(son)
    student = Student()
    student.make_program()  # 重写类方法(注释掉重写部分就是用继承的方法
    print(Student.mro())  # 打印父类信息
    student.make_program_master()  # 调用多继承的所有父类的同名方法
    student.make_program_school()
    student.make_program()
    sun = Sun()  # 多层继承通过__init__初始化后方法能正常调用
    sun.make_program()
    sun.make_program_school()
    sun.make_program_master()
    # student.__showMoney()#函数不存在
    print(student.getMoney())#通过非私有的方法访问私有属性
    student.set_money(100)
    print(student.getMoney())#成功修改私有属性
