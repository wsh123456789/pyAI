print("Hello World")

name = """ 
Hello World
11
"""

print(type(name))

name = "2+"
name += str(1)
print(name)
print(eval(name))


message = "Hello World %s 你好 %s" %(name, 1)
print(message)

print(f"{message[:3]}")

i = 1
for i in range(5):
    print(i)
print(i)


def add_demo(x, y):
    """
    说明文档
    :param x: 参数x
    :param y: 参数y
    :return: 返回和
    """
    print_demo()
    return x + y


def print_demo():
    print("Hello World")


add_demo(1, 2)


def demo_add(add_demo):
    return add_demo(1, 2)



