import random
# Homework 1
# 一个列表由4个元组组成，每个元组都是4个数字，对这个列表排序，按照元祖的第二个元素排序
li = []
for i in range(4):
    li.append((random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)))

print(f'排序前的列表为：{li}')

def sort_by_second(*args):
    li5 = []
    for i in args:
        li5.append((i[1], i))
    li5.sort()
    sorted_list = []
    for i in li5:
        sorted_list.append(i[1])
    return sorted_list
    
li = sort_by_second(*li)
print(f'排序后的列表为：{li}')

# Homework 2
# 定义一个函数，输入字符串，如果是顺序的返回UP，如果是倒序的返回DOWN，乱序的返回False
# def check_order(s):
#     if s == ''.join(sorted(s)):
#         return 'UP'
#     elif s == ''.join(sorted(s, reverse=True)):
#         return 'DOWN'
#     else:
#         return False