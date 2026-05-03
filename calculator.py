#1. 定义加减乘除运算函数
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    """除数运算，处理除数为零的情况"""
    if b == 0:
        raise ZeroDivisionError("除数不能为零，请重新输入")
    return a / b
#2. 运算符与函数映射（后续扩展新运算只需修改这里）
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
#3. 欢迎界面
print("欢迎使用简易计算器！")
print("支持的运算符：+  -  *  /")
print("输入格式：数字 运算符 数字（例如：3 + 5）")
print("输入 'exit' 退出程序")
#4. 主循环：支持多次运算，直到用户选择退出
while True:
    # 获取第一个数字
    num1_input = input("请输入第一个数字：")
    if num1_input.lower() == 'exit':
        print("感谢使用，再见！")
        break
    # 处理非数字输入异常
    try:
        num1 = float(num1_input)
    except ValueError:
        print("输入无效，请输入一个数字或'exit'退出！\n")
        continue
    # 获取运算符
    op = input("请输入运算符（+、-、*、/）：")
    if op not in operations:
        print("无效的运算符，请输入 +、-、* 或 /！\n")
        continue
    # 获取第二个数字
    num2_input = input("请输入第二个数字：")
    if num2_input.lower() == 'exit':
        print("感谢使用，再见！")
        break
    # 处理非数字输入异常
    try:
        num2 = float(num2_input)
    except ValueError:
        print("输入无效，请输入一个数字或'exit'退出！\n")
        continue
    #5. 执行运算并处理可能的异常（如除数为零）
    try:
        result = operations[op](num1, num2)
        print(f"结果：{num1} {op} {num2} = {result}\n")
    except ZeroDivisionError as e:
        print(f"错误：{e}\n")