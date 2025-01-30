class Dog:
    def work(self):
        print("我是狗")


class Dog_watch(Dog):  # 看门狗
    def work(self):
        print("看门")


class Dog_jing(Dog):  # 警犬
    def work(self):
        print("执行任务")


class People(object):
    def work_with_dog(self, dog):
        dog.work()


if __name__ == '__main__':
    people = People()
    dog1 = Dog_watch()
    people.work_with_dog(dog1)
    dog2 = Dog_jing()
    people.work_with_dog(dog2)
