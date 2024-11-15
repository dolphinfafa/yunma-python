# 输入三个数，判断输出最大的数值（不考虑两个数字相等情况）

# 方法一：用if完成
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
num3 = int(input("请输入第三个数："))
max_num = num1
if num2 > max_num:
    max_num = num2
if num3 > max_num:
    max_num = num3
print(f"最大的数值为：{max_num}")

# 方法二：用max函数完成
num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))
num3 = int(input("请输入第三个数："))
max_num = max(num1, num2, num3)
print(f"最大的数值为：{max_num}")



