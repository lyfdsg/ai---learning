# Function Basics:封装重复代码的最小单元
# 定义函数
# def function_name(参数1,参数2,...):
# """函数文档字符串(说明这个函数做什么的)"""
#   函数体（要执行的代码）
#   return 返回值 （可选，没有return语句时默认返回None）
# 调用函数
# 结果等于函数名(实参1,实参2,...)
# 定义一个函数，计算两个数的和
def add(a, b):
    """计算两个数的和"""
    return a + b
# 调用函数
result = add(3, 5)
print(result)  # 输出: 8

# 参数的五种类型
# 1. 位置参数（Positional Arguments）
# 2. 关键字参数（Keyword Arguments）
# 3. 默认参数（Default Arguments）
# 4. 可变参数（Variable Arguments）
# 5. 关键字可变参数（Keyword Variable Arguments）

# 位置参数
def greet(name, age):
    """使用位置参数打招呼"""
    print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30)  # 输出: Hello, Alice! You are 30 years old.
# 关键字参数与位置参数的区别
greet(name="Alice", age=30)  # 输出: Hello, Alice! You are 30 years old.
greet(age=30, name="Alice")  # 输出: Hello, Alice! You are 30 years old.
# 默认参数
def greet(name, age=25):
    """使用默认参数打招呼"""
    print(f"Hello, {name}! You are {age} years old.")
greet("Bob")  # 输出: Hello, Bob! You are 25 years old.
# 覆盖默认参数
greet("Bob", 35)  # 输出: Hello, Bob! You are 35 years old.
# 可变参数 *args，允许函数接受任意数量的位置参数，并将它们作为一个元组传递给函数，
# 再说明：*args 是一个约定俗成的名字，实际上你可以使用任何合法的变量名来代替它，
# 但 *args 已经成为了一个广泛接受的标准。
# 除了计算和之外，还可以使用 *args 来处理其他类型的可变参数，例如连接字符串、处理列表等。
# 目前还没有完全掌握 *args 的使用，后续会继续学习和练习。
def sum_all(*args):
    """计算所有参数的和"""
    return sum(args)
print(sum_all(1, 2, 3, 4, 5))  # 输出: 15
# 关键字可变参数 **kwargs，允许函数接受任意数量的关键字参数，并将它们作为一个字典传递给函数。
def print_info(**kwargs):
    """打印所有关键字参数的信息"""
    for key, value in kwargs.items():
        print(f"{key}: {value}") 
print_info(name="Alice", age=30, city="New York")
# 输出:
# name: Alice
# age: 30
# city: New York

# 函数的返回值：
# return 语句用于从函数中返回一个值，并结束函数的执行。
# 当函数被调用时，返回值可以被赋值给一个变量，或者直接使用。
def square(x):
    """返回一个数的平方"""
    return x * x
result = square(5)
print(result)  # 输出: 25   
# 函数没有 return 语句时，默认返回 None
def greet(name):
    """打招呼但不返回任何值"""
    print(f"Hello, {name}!")
result = greet("Alice")
print(result)  # 输出: None

# 作用域：局部作用域和全局作用域
# 局部作用域：函数内部定义的变量只能在函数内部访问，称为局部变量。
def my_function():
    local_var = "I am a local variable"
    print(local_var)          
my_function()  # 输出: I am a local variable  
# 为啥要有这行代码？因为 local_var 是局部变量，
# 为啥local_var 是局部变量？因为它是在函数内部定义的，所以它只能在函数内部访问。
# 为啥只能在函数内部访问？因为局部变量的作用域仅限于定义它的函数内部，函数外部无法访问它。
# 怎么样做到函数内部访问呢？
# 在函数内部定义一个变量 local_var，并打印它，这样就可以访问到这个局部变量了。
# 为啥下一行代码要写这个函数呢 ？
# 因为如果不调用这个函数，local_var 就不会被定义，也就无法访问它了。
# 必须在函数内部访问才能使用它，否则会报错。
# print(local_var)  # 这行代码会报错，因为 local_var 是局部变量，无法在函数外部访问

# 全局作用域：在函数外部定义的变量可以在整个程序中访问，称为全局变量。
global_var = "I am a global variable"
def my_function():
    print(global_var)
my_function()  # 输出: I am a global variable 
#这里为啥要写一个局部作用域的函数呢？因为我们需要在函数内部访问全局变量 global_var。
print(global_var)  # 输出: I am a global variable
# 在函数内部修改全局变量需要使用 global 关键字
counter = 0
def increment():
    global counter  # 声明 counter 是全局变量
    counter += 1    
increment()
print(counter)  # 输出: 1   
# 内部变量不应该是函数内部访问吗？为啥在函数外部打印 counter 也能访问到呢？
# 因为 counter 是一个全局变量，定义在函数外部，所以它可以在整个程序中访问，包括函数内部和外部。

# 匿名函数（Lambda Functions）：
# 匿名函数是一种没有名字的函数，通常用于需要一个简单函数作为参数的场景。
# 使用 lambda 关键字定义匿名函数。
square = lambda x: x * x
print(square(5))  # 输出: 25 
# 定义匿名函数只需要赋值给一个变量就可以了，不需要使用 def 关键字。
# 匿名函数也可以接受多个参数
add = lambda a, b: a + b
print(add(3, 5))  # 输出: 8
# 匿名函数通常用于需要一个简单函数作为参数的场景，例如在排序、过滤等操作中。
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # 输出: [1, 4, 9, 16, 25]
# 这里使用了 map 函数和一个匿名函数来计算 numbers 列表中每个元素的平方，
# 并将结果转换为一个新的列表 squared_numbers。什么是 map 函数？
# map 函数是 Python 内置的一个高阶函数，它接受一个函数和一个可迭代对象（如列表、元组等）作为参数，
# 并将函数应用于可迭代对象的每个元素，返回一个新的迭代器。

# 错误写法
def add_item(item, lst=[]):
    """将一个元素添加到列表中"""
    lst.append(item)
    return lst

print(add_item(1))  # 输出: [1]
print(add_item(2))  # 输出: [1, 2] (预期是 [2]，因为默认参数只在函数定义时创建一次)
#这里为啥是 [1, 2] 呢？
# 因为默认参数 lst=[] 只在函数定义时创建一次，所以当第一次调用 add_item(1) 时，lst 被修改为 [1]。
# 当第二次调用 add_item(2) 时，lst 已经是 [1] 了，所以它会继续修改这个列表，最终变成 [1, 2]。

# 正确写法
def add_item(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
print(add_item(1))  # 输出: [1]
print(add_item(2))  # 输出: [2] (每次调用都会创建一个新的列表)
# 这里使用了 None 作为默认参数值，
# 并在函数内部检查 lst 是否为 None，
# 如果是，则创建一个新的列表。这样每次调用 add_item 都会使用一个新的列表，避免了之前的问题。