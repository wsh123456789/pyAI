# len() 获取变量长度
name = "it monkey"
print(len(name))


# def 函数名(参数):
#     函数体
#     return 返回值
def my_len(string):
    print(f"字符串长度为{len(string)}")


my_len(name)


# class 类名()
#       def 函数名(参数):
#           函数体
#           return 返回值
class Length:
    def my_len(self):
        print(len(self))


Length.my_len(name)


# 列表(list), 元组(tuple), 字符串(str), 集合(set), 字典(dict)

# ------------------------------------------------------------------
# list列表   容量为 2**63-1 == 9223372036854775807
# 可容纳不同类型元素
# 数据有序储存 (有下标)
# 允许数据重复存在
# 可修改
name_list = ['liming', 'Jenny', 'Danny', [1, 2, 3]]
# 空列表
list_null = []
list_null = list()
print(name_list[-3])
print(name_list[3])
print(name_list[3][0])

# index(元素) 查找指定元素在列表的下标，找不到报错ValueError
index = name_list.index("Danny")
print(f"Danny的下标为{index}")
# print(f"报错{name_list.index('a')}")

# 修改第一个值
print(f"修改前 {name_list[0]}")
name_list[0] = 1
print(f"修改后 {name_list[0]}")

# 插入 List.insert(下标, 值)
print(f"插入前: {name_list}")
name_list.insert(1, "liming")
print(f"插入后: {name_list}")

# 尾部追加单个元素 List.append(value)
print(f"追加前: {name_list}")
name_list.append([4, 5, 6])
name_list.append(7)
print(f"追加后: {name_list}")

# 尾部追加多个元素 List.extend(value)
my_list = [1, 2, 3, 4]
my_list.extend([5, 6, 7])
print(f"追加后:{my_list}")

# 删除元素 del List[n]
del my_list[1]
print(f"删除(del方法)后:{my_list}")

my_list.pop(2)
print(f"删除后(pop方法):{my_list}")

# 删除某元素在列表中的第一个匹配项 List.remove(value)
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print(f"删除后(remove方法):{my_list}")

# 清空列表 List.clear()
my_list.clear()
print(f"清空后:{my_list}")

# 计算某元素在列表内的数量 List.count(value)
my_list = [1, 2, 3, 2, 4, 2]
count = my_list.count(2)
print(f"元素2在列表中的数量为：{count}")

# 计算列表的长度(列表元素数量)
print(f"列表长度为:{len(my_list)} \n {my_list}")

# 反转列表 list.reverse() 会改变原列表
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(f"反转后为{my_list}")
# ------------------------------------------------------------------
# 元组(tuple) 一旦定义就不修改 其余和列表相同
t1 = (1, 2, "hello", True)
t2 = ()
t3 = tuple()
print(f"t1类型是: {type(t1)}, 内容是 {t1}")
print(f"t2类型是: {type(t2)}, 内容是 {t2}")
print(f"t3类型是: {type(t3)}, 内容是 {t3}")
# 定义元组只有一个元素时在元素后加逗号，否则定义的单元素元组为元素的类型
# 查找元组元素下标 tuple.index(value)
# 统计元组中某个元素出现的次数 tuple.count(value)
# 计算元组长度 len(tuple)
t4 = ("hello")
# t4类型是: <class 'str'>, 内容是 hello
print(f"t4类型是: {type(t4)}, 内容是 {t4}")
t4 = ("hello", )
# t4类型是: <class 'tuple'>, 内容是 ('hello',)
print(f"t4类型是: {type(t4)}, 内容是 {t4}")
t4 = ((1, 2, 3), (4, 5, 6))
print(f"t4类型是: {type(t4)}, 内容是 {t4}")
# 从t4取元组值 6
print(t4[1][2])

# 元组不可修改，但是内嵌的list可以修改
t5 = (1, 2, 3, [3, 4, 5], 6, 7, 8)
# t5[1] = 1 结果为(TypeError: 'tuple' object does not support item assignment/)
print(f"t5修改前：{t5}")
t5[3][0] = 9
print(f"t5修改后：{t5}")

# ------------------------------------------------------------------
# 字符串 str 不可修改
str1 = "IT monkey"
print(str1.index("m"))

# 字符串替换 replace   str.replace(str1, str2) 把str里的str1替换为str2
# 此方法会生成一个新的字符串，不会改变str1
str2 = str1.replace("monkey", "dog")
print(f"替换后：str1为{str1} str2为{str2}")

# 字符串分割 split     str.split(参数) 按照参数分割字符串生成一个新列表
new_list = str1.split(" ")
print(f"分割结果为{new_list}")

# 字符串规整操作 str.strip(参数) 把字符串开头结尾与参数值相同的值剔除
# 不穿参默认去除前后空格
str3 = " IT monkey "
print(str3.strip())
# 去除字符串开头结尾在参数中所有出现过的字符
str3 = "12IT 12 monkey12"
# IT 12 monkey
print(str3.strip("12"))

# 统计子串在字符串中出现的次数 str.count(str)
str4 = "it it monkey it"
count = str4.count("it")
print(f"it在str4字符串中出现的次数为{count}")

# 计算字符串长度 len(str)
length = len(str4)
print(f"str4字符串长度为{length}")

# capiatlize : 首字母大写，可以把字符串的第一个字母大写
print(str4.capitalize())
# title : 将字符串中的每个单词的首字母大写
print(str4.title())
# lower : 把字符串全部转为小写
# upper : 把字符串全部转为大写
print(f"全部转为小写：{str4.lower()}")
print(f"全部转为大写：{str4.upper()}")
# join : 连接字符串， 将一个字符串拼接到列表中，返回字符串
li = ["1", "b", "c"]
s = ["abc",  "def"]

str2 = "abcsd"
str4 = str2.join(li)
# 1 abcsd b abcsd c
print(str4)
# 四、调试与删除功能
# # ljust : left just, 左对齐、并且将字符串调整至指定长度
# print(str2.ljust(10,"*"))
# # rjust: right just, 右对齐、并且将字符串调整至指定长度
# print(str2.rjust(10,"-"))
# # center : 居中对齐、并且将字符串调整至指定长度
# print(str2.center(11,"."))
#
# str3 = "  abc , def  "
# # strip : 删除字符串两端的空白字符
print(str3.strip())
# # lstrip : left strip，删除左边的空白字符
# print(str3.lstrip())
# # rstrip : right strip，删除右边的空白字符
# print(str3.rstrip())

str4 = "abcAacc艾哈12"
# 五、判断功能  bool
# startswith : 从..开始，判断字符串是否以指定的文字开头
# print(str4.startswith("bc Aacb"))
# endswith : 以..结束，判断字符串是否以指定的文字结尾
# print(str4.endswith("Aac"))
# isalpha : alpha 字母，判断是否所有的字符都是字母（中文），是为true
print(str4.isalpha())
# isdigit : digit 数字，判断字符串中是否全都是数字 是为true
str5 = "123a22"
print(str5.isdigit())
# isalnum : alpha number，判断字符串中是否全都是字母(中文)或数字，是为true
print(str5.isalnum())
# isspace ： space 空白，判断字符串中是否只包含空格(换行符)，
str6 = "        ."
print(str6.isspace())

# 序列切片 str[start:end [, step] ]反向取值需要范围对调
print(str4[5: 1: -1])

# ------------------------------------------------------------------

# 集合 set
# 集合是无序的，不支持下标索引，自动去重，可修改
# 集合只能包含数字，字符串，元组等不可变类型数据，不能包含列表，字典，集合等可变序列的数据

# 集合的添加
# s.add(5)
# s.update(100) # 需要传入可迭代对象 拆分添加

# 删除
# s.remove(23) # 元素不存在则报错
# s.pop() # 随机删除，删除的是左边 第一个
# s.discard(23) # 不存在就不删除

my_set = {"礼炮", "it monkey", "老人与海", "礼炮", "it monkey", "老人与海"}
my_set_empty = {}
my_set_empty = set()
print(f"my_set内容是: {my_set}类型是 {type(my_set)}")
print(f"my_set_empty内容是: {my_set_empty}类型是 {type(my_set_empty)}")
# 添加元素 set.add(value)
my_set.add("python")
print(my_set)
# 随机取出一个元素 set.pop()
element = my_set.pop()
print(f"集合被取出的元素{element} 取出元素后的集合为:{my_set}")
# 清空集合 set.clear()
my_set.clear()
print(f"清空后的集合为:{my_set}")
# 取出两个集合的差值 set1.difference(set2) 取出set1有set2没有的值
# 不影响set1 和 set2的值
set1 = {1, 2, 3, 4}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(f"set1的值为：{set1}")
print(f"set2的值为：{set2}")
print(f"set1有而set2没有的值为: {set3}")
# 消除交集  set1.difference_update(set2)  会改变set1的值
set1 = {1, 2, 3, 4}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(f"set1的值为：{set1}")
print(f"set2的值为：{set2}")
# 合并集合 set3 = set1.union(set2)  不影响set1 和 set2的值
set1 = {1, 2, 3, 4}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(f"set1的值为：{set1}")
print(f"set2的值为：{set2}")
print(f"合并后为:{set3}")
# len()统计集合元素数量
print(f"元素数量为{len(set3)}")
set4 = {1, 2, (6, 7, 8)}
print(f"元素数量为{len(set4)}")
# 集合的遍历 集合没有下标不能用while遍历，只能使用for循环遍历

# ------------------------------------------------------------------
# 字典 dict
# 空字典
# 字典不允许 列表， 字典，集合作为key值
my_dict = {}
my_dict = dict()
print(f"字典内容为: {my_dict}\n 字典类型为{type(my_dict)}")
dic = {'HAHA', 'day'}
# 字典不允许key值重复，后定义的key会覆盖先定义的key
my_dict = {
    "name": "liming",
    "score": 90,
    "hobby": "唱歌",
    "score": 99
}
print(f"字典内容为:{my_dict}\n姓名为{my_dict['name']}")
# key值不可以为字典，value可以为字典
my_dict = {
    "liming": {
        "语文": 99,
        "数学": 92,
        "英语": 89
    },
    "Danny": {
        "语文": 99,
        "数学": 92,
        "英语": 89
    },
    "Jenny": {
        "语文": 99,
        "数学": 92,
        "英语": 89
    }
}
print(f"字典内容为:{my_dict}\nJenny成绩为: {my_dict['Jenny']}\nDanny的数学成绩为: {my_dict['Danny']['数学']}")
# 新增元素
my_dict = {
    "name": "liming",
    "score": 90,
    "hobby": "唱歌"
}
my_dict["money"] = 100
print(my_dict)

# 删除字典元素 dict.pop(key)
my_dict.pop('name')
print(my_dict)

# 清空字典 dist.clear()
my_dict.clear()
print(my_dict)

# 获取字典中全部key值
my_dict = {
    "name": "liming",
    "score": 90,
    "hobby": "唱歌"
}
keys = my_dict.keys()
print(f"字典中的全部key值为: {keys}")

# dict.setdefault(key, default) 存在就查询，不存在就添加 键不存在时，默认值为default
print(my_dict.setdefault("name", 0))

# 遍历字典
for key in keys:
    print(f"字典的key是: {key}\t字典的value是: {my_dict[key]}")
# 拆包
for i, j in enumerate(my_dict,100):
    print(i, j)
# 计算字典长度len(my_dist)

# 排序 正常排序会改变原值，反转时不改变原值
set1 = {2, 1, 4, 3}
set2 = sorted(set1, reverse=True)
print(set1)
print(set2)
