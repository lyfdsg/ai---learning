# 定义变量 变量命名规则
name = "刘宇飞"
age = 24
height = 170.0
is_learning = True
print("我的名字是", name)
print("我的年龄是", age)
print("我的身高是", height)
print("我正在学习吗？", is_learning)
# 怎么看变量类型
print(type(name))
print(type(age))
print(type(height))
print(type(is_learning))
# 变量类型转换
  # 将字符串转换为整数
age_str = "24"
age_num = int(age_str)
print(age_num + 1)# 输出 25
  # 将整数转换为字符串
print("我今年" + str(age) + "岁了")# 输出 我今年24岁了
  # 将字符串转换为浮点数
height_str = "170.0"
height_num = float(height_str)
print(height_num + 10.0)# 输出 180.0
  # 整数转浮点数
print(float(age))# 输出 24.0
# 赋值运算符（简称赋值）
a = 10
a += 3  # 等价于 a = a + 3 a变成13
a -= 2  # 等价于 a = a - 2 a变成11
a *= 2  # 等价于 a = a * 2 a变成22
a /= 2  # 等价于 a = a / 2 a变成11.0(注意变成了浮点数)
# 变量+数据类型+运算符综合练习
name = "王萍"
age = 22
height = 158.0
weight = 39.25

# 1.算数运算：计算女朋友的BMI指数（体重kg/身高m的平方）
bmi = weight / (height / 100) ** 2
print("女朋友的BMI指数是：", bmi)
# 2.比较运算：判断女朋友的BMI指数是否正常（正常范围18.5-24.9）
is_bmi_normal = 18.5 <= bmi <= 24.9
print("女朋友的BMI指数正常吗？", is_bmi_normal)