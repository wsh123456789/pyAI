def user_info(name, age, sex):
    print(f"您的名字是{name}, 年龄是{age}, 性别是{sex}")


user_info("老人与海", 22, "男")


# 不定长参数
# *args 接受参数合并为元组
def user_info(*args):
    print(args)


user_info("tom", 18, "男")


# **kwargs 参数为 key = value 接受参数合并为字典
def user_info(**kwargs):
    print(kwargs)


user_info(name="tom", age=18, sex="男")


# 函数调用(嵌套)
def text_func():
    result = compute(1, 2)
    print(result)


def compute(x, y):
    return x + y


text_func()

# 匿名函数 lambda 用于简单的定义，只能写一行
addn = lambda x, y: x + y
print(addn(1, 2))

# open(name, mode, encoding)
# name: 要打开的目标文件名的字符串(可以包含文件所在的具体路径)
# mode: 设置打开文件的的模式(访问模式): 只读，写入，追加等。
#       r: 只读
#       w: 从第一行开始写入，如果没有此文档则创建新文档
#       a: 文件不存在创建文件，文件存在则在最后追加写入文件
# ending: 编码格式(默认UTF-8)
# f = open("text", "r", encoding="UTF-8")
# print(type(f))
# 读取文件
# 文件对象.read(num): num表示要读取对象的数据长度(单位为字节), 如果没有传入num， 默认读取整个文件
# 文件对象.readline(): 调用一次读取一行结果
# 文件对象.readlines(): 按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行的数据为一个元素

# print(f"read()读取十个字节的结果:\t{f.read(10)}")

# print(f"第一行为:{f.readline()}")
# print(f"第二行为:{f.readline()}")

# 多次读取时，后一次读取会从上次读取结束的位置开始
# print(f"read()读取全部内容的结果:\t{f.read()}")

# print(f"readlines()读取结果的类型: {type(f.readlines())}")
# print(f"readlines()读取结果为{f.readlines()}")

# for循环可以遍历文件，每个元素为一行
# for line in f:
#     print(line)

# 关闭文件 文件对象.close()
# f.close()

# 文件睡眠， 会一直占用文件: 文件对象.sleep(time)

# with open 语法  执行完成自动关闭文件
# with open("text", "r", encoding="UTF-8") as f:
#     print(f.readlines())

# 文件写入 文件对象.write(element) 文件不会直接写入文件中，会存到内存的缓冲区，经过刷新处理后才会写入文件
# 文件刷新 文件对象.flush()

# 将python转为json
import json

data = [{"name": "张大山", "age": 19}, {"name": "王大锤", "age": 18}, {"name": "赵小虎", "age": 17}]
json_str = json.dumps(data, ensure_ascii=False)
print(type(json_str))
print(json_str)

# 将json转换为python
s = '[{"name": "张大山", "age": 19}, {"name": "王大锤", "age": 18}, {"name": "赵小虎", "age": 17}]'
li = json.loads(s)
print(type(li))
print(li)

# 列表推导式
li = [i for i in range(10)]
print(li)
li = [(i, j) for i in range(2) for j in range(10, 0, -1)]
print(li)

# map函数
my_list = [1, 2, 3, 4, 5]


def f(x):
    return x ** 2


result = map(f, my_list)
print(type(result), result, list(result))  # <class 'map'> <map object at 0x00000287F8323040> [1, 4, 9, 16, 25]

# reduce函数
import functools

my_list = [1, 2, 3, 4, 5]


def f(x1, x2):
    return x1 + x2


result = functools.reduce(f, my_list)
print(result)  # 15

# filter过滤函数
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def f(x):
    return x % 2 == 0


result = filter(f, my_list)
print(list(result))