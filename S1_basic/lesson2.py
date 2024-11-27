# 让用户输入半径，计算出对应圆的周长与面积
# 提升：结果保留两位小数
import math

radius = float(input("请输入半径："))
perimeter = 2 * math.pi * radius
area = math.pi * radius ** 2
print(f"该圆的周长为：{perimeter:.2f}")
print(f"该圆的面积为：{area:.2f}")
