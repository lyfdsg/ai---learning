# 单条件
# if 条件:
#     条件成立时执行的代码

# 二选一
# if 条件：
#    条件成立时执行的代码
# else:
#    条件不成立时执行的代码

# 多条件判断
# if 条件1：
#     条件1成立时执行的代码
# elif 条件2:
#     条件2成立时执行的代码
# elif 条件3:
#     条件3成立时执行的代码
# else:
#     条件1、条件2、条件3都不成立时执行的代码
age = 18
if age >= 18:
    print("成年了")
else:
    print("未成年")

# while 条件：
#     条件成立时重复执行的代码
while True:
    num = input("请输入内容：")
    print("你输入了：", num)
    continue_input = input("是否继续输入？(y/n): ")
#如果用户输入的不是 'y'（不区分大小写），就退出循环。
# .lower() 是一个字符串方法，用于将字符串中的所有字符转换为小写字母。
# 这样，无论用户输入的是 'Y' 还是 'y'，都能正确识别为继续输入的指令。
# 为啥还要加入感叹号呢？因为感叹号在这里表示逻辑非（not），即当用户输入的不是 'y' 时，条件成立，执行退出循环的代码。      
    if continue_input.lower() != 'y': 
        print("退出循环")
        break  

# for 变量 in 可迭代对象:
for i in range(5):
    print("第",i,"次循环")

# break 退出循环
# continue 跳过本次循环，继续下一次循环
while True:
    expr = input("请输入一个数字，输入q退出：")
    if expr == 'q':
        print("退出循环")
        break
    # 条件判断：非空就计算
    if expr:
        res = eval(expr)
        print("计算结果：", res)
    else:
        print("输入不能为空，请重新输入")
        continue