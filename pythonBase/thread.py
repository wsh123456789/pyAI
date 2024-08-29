import threading
# 属性值
# group: 暂时没有用处，未来预留的参数
# target: 执行的目标任务名
# args: 以元组的形式给执行任务传参
# kwargs: 以字典的方式给执行任务传参
# name: 线程名，一般不用设置


def thread_sing():
    print("唱")


def thread_dance():
    print("跳舞")


thread_obj = threading.Thread(target=thread_sing)
thread_obj.start()



