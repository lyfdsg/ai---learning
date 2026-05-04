import math_utils

print(math_utils.PI)
print(math_utils.add(5, 3))
print(math_utils.multiply(5, 3))

# 导入模块并起别名
import math_utils as mu
print(mu.PI)
print(mu.add(10, 20))   
print(mu.multiply(10, 20))

# 导入模块中所有内容
from math_utils import *
print(PI)
print(add(5, 3))
print(multiply(5, 3))