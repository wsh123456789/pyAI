# 模块 from... import... as...

# 导入time模块
import time
print("你好")
time.sleep(3)
print("hello")

# 只导入time的sleep 导入全部 from time import *
from time import sleep
print("你好")
sleep(3)
print("hello")

import model_package.model01 as model01
import model_package.model02 as model02

model01
model02

# 只在主函数文件执行，被调时不执行
if __name__ == "__main__":
    print("主函数")

# __all__ = ['a']   用import * 导入时只能使用a方法

import python_base.error as error
error.main()
