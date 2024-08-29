# 简单闭包
def outer(logo):
    def inner(msg):
        print(f"{logo} -- {msg}")

    return inner


fn1 = outer("Hello")
fn1("world")


# 如果想修改外部函数传来的值 例如 logo 需要用nonlocal声明变量
def outer(logo):
    def inner(msg):
        nonlocal logo
        logo = "你好"
        print(f"{logo} -- {msg}")

    return inner


fn1 = outer("Hello")
fn1("world")


# 装饰器
def outer(func):
    def inner():
        print("打开电脑")
        func()
        print("关闭电脑")
    return inner


def sleep():
    import time
    import random
    print("玩黑神话")
    time.sleep(random.randint(1, 5))


fn = outer(sleep)
fn()
