class Student:
    name = None
    sex = None
    nationality = None
    native_place = None
    age = None

    # __init__ 方法会自动执行，有此方法必须传参
    def __init__(self, name, sex, nationality, native_place, age):
        self.name = name
        self.sex = sex
        self.nationality = nationality
        self.native_place = native_place
        self.age = age
        print("创建成功！！！")

    def say_hi(self):
        print(f"你好,{self.name}")

    def say_hi01(self, msg):
        print(f"你好,{msg}")


# stu1 = Student()
#
# stu1.name = "坤坤"
# stu1.sex = "公"
# stu1.nationality = "坤国"
# stu1.native_place = "坤省"
# stu1.age = 25
#
# print(stu1.name)
# print(stu1.sex)
# print(stu1.nationality)
# print(stu1.native_place)
# print(stu1.age)

# stu1.say_hi()
# stu1.say_hi01("老人于海")

stu2 = Student("老人与海", "不详", "中国", "北京", 19)
print(stu2.name)
print(stu2.sex)
print(stu2.nationality)
print(stu2.native_place)
print(stu2.age)


# 常用内置方法
class Demo:
    # 构造方法，可用于创建类对象的时候设置初始化行为
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"我是__init__构造方法")

    # 用于类对象转字符串的行为
    def __str__(self):
        return f"Demo类对象， name={self.name}，age={self.age}"

    # __lt__ 方法判断大小
    def __lt__(self, other):
        return f"__lt__ 方法比较结果: {self.age < other.age}"

    # __le__ 方法判断大于等于或小于等于
    def __le__(self, other):
        return f"__le__ 方法比较结果: {self.age <= other.age}"

    # __eq__ 方法判断是否相等
    def __eq__(self, other):
        return f"__eq__ 方法比较结果: {self.age < other.age}"


demo1 = Demo("ikun", 23)
demo2 = Demo("iyu", 25)

print(demo1)
print(str(demo1))
print(demo1 > demo2)
print(demo1 <= demo2)
print(demo1 == demo2)


# 前边有__符号的为私有变量或方法，导包时不能直接使用

# 继承 单继承，多继承
class Phone():
    IMEI = "nihao"
    producer = "HM"

    def call_by_4g(self):
        print("4g通话", self.producer)

    def call_by_5g(self):
        print("父类5g")


class Phone2023(Phone):
    face_id = "10001"
    producer = "2023"

    def call_by_5g(self):
        print(f"父类变量:{super().producer}")
        super().call_by_5g()
        print("2023年新功能: 5g通话")

# phone = Phone2023()
# print(phone.producer)
# phone.call_by_4g()
# phone.call_by_5g()

class Phone2024(Phone2023):
    face_id = "102222"
    producer = "2024"
    ai = "AI发展迅猛"

    def call_by_5g(self):
        print(f"父类变量:{super().producer}")
        print(f"父类变量IMEI:{super().IMEI}")
        super().call_by_5g()
        print("2024年新功能: AI通话")

phone2 = Phone2024()
print(phone2.producer)
phone2.call_by_4g()
phone2.call_by_5g()
# 注解 my_list: list[int] = [1, 2, 3]
# 联合注解  my_list: list[Union[str,int]] = [1, 2, 'aa', 'bbb'] (需要导包 from typing import Union)

# 多态
class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal):
    animal.speak()


dog = Dog()
cat = Cat()
make_noise(dog)
make_noise(cat)
