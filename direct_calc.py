print("===== 表达式计算器 =====")
print("支持：加减乘除 +-*/")
print("输入 q 退出程序\n")
while True:
    exp = input("请输入表达式：")

    #退出程序
    if exp.lower() == 'q':
        print("程序退出！")
        break

    try:
        # 计算表达式
        res = eval(exp)
        print(f"计算结果：{res}\n")

    except ZeroDivisionError:
        print("错误：除数不能为0！\n")
    except SyntaxError:
        print("错误：表达式格式不正确！\n")
    except:
        print("错误：输入无效，请重新输入！\n")