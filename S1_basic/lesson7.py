# 列表中有重复元素，移除重复元素
list1 = [10, 12, 45, 10, 12, 12, 16, 15, 10]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)

list2.sort(reverse=True)
print(list2)