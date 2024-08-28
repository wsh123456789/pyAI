"""
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
    file 文件路径
    mode 文件的操作
    buffering 缓存区，暂时性存储数据
    encoding 编码格式
    errors 错误
    newline 换行
    closefd 关闭

W 写入模式
    每次都是重新写入，指针在文件的最前面
    write() 参数必须是str
    writelines（） 参数是可迭代对象,元素必须是str
    writable()  判断当前文件是否可以写入

R 读取模式
    指针在文件的最前面
    没编码读字节，有编码读字符
    read()  读全部
    readline() 读整行
    readlines() 将每行当成一个元素，最终会返回一个列表,只会整个读

"""
# 写入
# 1、创建写入对象，没有会创建
fd = open("ds.pa","w") # 句柄
# 2、写入内容
li = ["aa","bb","cc"]
fd.write("\nabvc")
fd.writelines(li)
print(fd.writable())
# 3、关闭资源
fd.close()

# 读取
# 1、创建读取对象，没有会报错
fd = open("aaa.txt", "r" ,encoding="utf-8")
#2、读取内容
# s = fd.read(10)
# s =fd.readline(3)
s = fd.readlines(7)
fd.readable()
print(s)


# 3、关闭资源
fd.close()


# fd = open("a.jpg","rb")
# s = fd.read()
# print(s)
# fd.close()
#
# fd2 = open("aCopy.jpg","wb")
# fd2.write(s)
# fd2.close()

# 可读可写
# fd = open("aa.txt","w+",encoding="utf-8")
# # fd.write("aaa小白兔\n")
# # fd.write("白又白")
# #
# # # utf-8  一个中文是3个字节  gbk 一个中文是两个字节
# # fd.seek(1,0) # 参数1 预留几个字节的位置 ，参数2 调整指针的位置 0从头读 1当前位置 2末尾
# # fd.write("db哈哈")
# # s = fd.read()
# # print(s)
# # fd.close()

fd = open("aa.txt","a",encoding="utf-8")
fd.seek(2,0) # a模式不能调整指针位置
fd.write("aaa")
fd.close()


# """
# W write 写入模式
#     每次都是重新写入，指针在文件的最前面
#     write() 参数必须是str
#     writelines（） 参数是可迭代对象,元素必须是str
#     writable()  判断当前文件是否可以写入
#
# R read 读取模式
#     指针在文件的最前面
#     没编码读字节，有编码读字符
#     read()  读全部
#     readline() 读整行
#     readlines() 将每行当成一个元素，最终会返回一个列表,只会整个读
#
# X xor 异或模式
#     不存在就创建，存在就报错，指针在最前面
#
# A append 追加模式
#     不存在就创建，存在就继续往后写，指针在文件的最后面
#
# 不能单独使用的模式
#     b binary 二进制模式
#     t text 文本模式（默认）
#     + 更新读写
# 套装
#     wb\rb\ab\xb 二进制的读写
#     w+\r+\a+\x+ 可读可写的操作普通文件
#     wb+\rb+\ab+\xb+  可读可写的操作二进制文件
# """



# fd = open("aaaa.txt","x",encoding="utf-8")
# fd.write("哈哈")
# fd.close()

# fd = open("aa.txt","a",encoding="utf-8")
# fd.write("美术老师")
# fd.close()