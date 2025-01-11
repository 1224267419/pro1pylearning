import time


def timing(f):  # 仅调用
    def wrapper():
        return f()

    return wrapper


def timing(f):  # 调用时的业务代码,可以修改,此处用计时现实运行时间
    def wrapper():
        start = time.time()
        res = f()
        print(f"{time.time() - start}")  # 运行时间
        return res

    return wrapper


def hello():  # 不允许修改
    print("enter hello")


@timing  # 此处的@timing装饰器等价于下面的 hello = timing(hello)语句
def hello():  # 不允许修改
    print("enter hello")


# hello = timing(hello)
print(hello)  # 此处wrapper指向hello的指针
hello()
