a = 12
b = [1, 2, 3, 4, 5, 6]
c = "1"
d = "c"
print(a)
print(b)
print(type(c))
c = int(c)
print(type(c))
name = "程序员"
message = "学IT变成: %s" % name
print(message)
num = 10
salary = 15.6
message = " %s 学费: %d k 工资: %.2f k" % (name, num, salary)
print(message)
print(f" {name} 学费: {num} k 工资: {salary} k")
# name = input()
# print(f"给 {name} 买瓜子")
# name = int(input("请输入整数\n"))
# print(type(name), name)
num = "10+20"
print(eval(num))
num1 = 1
num2 = 2
print(f"结果：{num1 > num2}")

if int(input("猜数字，请输入数字：\n")) == 1:
    print("第一次猜对了")
elif int(input("猜错了，还有一次机会：\n")) == 1:
    print("猜对了")
else:
    print("猜错了")

max = "10最大" if 10 > 20 else "20最大"
min = "10最小" if 10 < 20 else "20最小"
print(max)
print(min)

import random
num = random.randint(1, 10)
print(num)

i = 1
while i <= 2:
    print(f"i的值为{i}")
    i += 1

i = 1
num = 0
while i <= 100:
    num += i
    i = i + 1
print(num)
# 猜数字
import random
num = random.randint(0, 10)
count = 1
flag = True
while flag:
    guess_num = int(input(f"第{count}猜测:"))
    if guess_num == num:
        print(f"恭喜你猜对了,猜题次数为{count}")
        flag = False
    else:
        count += 1
        if guess_num > num:
            print("猜大了")
        else:
            print("猜小了")
# 九九乘法表
# while循环实现
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f"{j}*{i}={i*j}\t", end="")
        j += 1
    print()
    i += 1
# for循环实现
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={i * j}\t", end="")
    print()

name = [1, 2, 3, 4, 5]
for i in name:
    print(i)

# range(end): 从零开始到end-1
# range(start, end [, step])  数组不包含end   step表示步长(间隔)
arr1 = range(1, 10, 2)
for i in arr1:
    print(i)
