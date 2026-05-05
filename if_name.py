# 通过编辑包my_tool中的__init__.py文件，
# 我们可以将math_utils模块中的变量和函数直接导入到包的命名空间中，
# 这样在使用if_name.py时就可以直接使用PI、add和multiply，而不需要再通过math_utils来访问它们。
from my_tool import PI, add , multiply 
print("This is if_name.py, and we have imported math_utils from my_tool.", PI, add(2, 3), multiply(4, 5))


PI = 3.14159

def add(a, b):
    return a + b

# 只有当直接运行这个文件时，下面的代码才会被执行
# 当被其他文件导入时，下面的代码不会被执行
if __name__ == '__main__':#上面导入了模块 math_utils，所以在这个文件中可以直接使用 math_utils 中定义的变量和函数，例如 PI 和 add。
# 但这个if 条件是不成立的呀？因为这个文件被导入了，所以 __name__ 的值是 'if_name'，而不是 '__main__'，所以这个条件不成立，下面的代码不会被执行。
# 当直接运行这个文件时，__name__ 的值是 '__main__'，所以这个条件成立，下面的代码会被执行。 
# 上面这行代码的意思是：如果这个文件是被直接运行的，那么就执行下面的代码
# __name__ 是一个特殊变量，它表示当前模块的名字
# 当直接运行这个文件时，__name__ 的值是 '__main__'
# _main_ 是 Python 解释器为直接运行的模块设置的特殊名字
    print("This code is running directly.")
    print("PI:", PI)
    print("add(2, 3):", add(2, 3))