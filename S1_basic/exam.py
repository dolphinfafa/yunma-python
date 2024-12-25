# 第一题
# 一个列表，里面都是整数，要求删除一个元素，使得剩余元素的乘积最大(需要考虑是否有负数存在)
li = [1, 2, 3, -4, 5, 6, 7, 8, 9]
delete_result = []
for i in range(len(li)):
    temp = li.copy()
    temp.pop(i)
    result = 1
    for j in temp:
        result *= j
    delete_result.append([result, i])
# 对结果进行排序
delete_result.sort(reverse=True)
print(f'删除第{delete_result[0][1]}个元素后，剩余元素的乘积最大,结果为{delete_result[0][0]}')

# 第二题
# a_list = [1,2,3,4,5,6,7,8,9]. 请写出你想到最精简的代码
# 1、请把每个项元素都+1
# 2、将其中的偶数去除掉
# 3、再把list中每个元素相乘
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = 1
for i in a_list:
    if i % 2 != 0:
        result *= i + 1
print(result)

# 第三题
# 给定一个列表和一个值，列表中数字两两相加如果
# 有等于这个值的，就返回这两个值的索引，
# 否则返回[-1, -1],比如：
# 1. 给定列表[1, 5, 7, 20], 给定值12，返回[1,2]
# 2. 给定列表[1, 2, 6, 8 ], 给定值2，返回[-1, -1]

# li = [1, 5, 7, 20]
# value = 12
li = [1, 2, 6, 8]
value = 2
for i in range(len(li)):
    for j in range(i + 1, len(li)):
        if li[i] + li[j] == value:
            print([i, j])
            break
    else:
        continue
    break
else:
    print([-1, -1])

# 第四题
# 定义一个类，可以对输入的文章进行统计，要求实现以下几个方法：
#     1. 统计出各个单词出现的次数和频率
#     2. 查看出现频率最多的前10个单词
#     3. 输入单词能够得到单词的出现次数和频率
str = '''
There are moments in life when you miss someone so much that you just want to pick them from your dreams and hug them for real! Dream what you want to dream;go where you want to go;be what you want to be,because you have only one life and one chance to do all the things you want to do.
May you have enough happiness to make you sweet,enough trials to make you strong,enough sorrow to keep you human,enough hope to make you happy? Always put yourself in others’shoes.If you feel that it hurts you,it probably hurts the other person, too.
The happiest of people don’t necessarily have the best of everything;they just make the most of everything that comes along their way.Happiness lies for those who cry,those who hurt, those who have searched,and those who have tried,for only they can appreciate the importance of people
who have touched their lives.Love begins with a smile,grows with a kiss and ends with a tear.The brightest future will always be based on a forgotten past, you can’t go on well in lifeuntil you let go of your past failures and heartaches.
When you were born,you were crying and everyone around you was smiling.Live your life so that when you die,you're the one who is smiling and everyone around you is crying.
Please send this message to those people who mean something to you,to those who have touched your life in one way or another,to those who make you smile when you really need it,to those that make you see the brighter side of things when you are really down,to those who you want to let them know that you appreciate their friendship.And if you don’t, don’t worry,nothing bad will happen to you,you will just miss out on the opportunity to brighten someone’s day with this message.
'''
import re
dic = {}
# 通过正则找到str中的所有单词，并统计出现次数
words = re.findall(r'\b\w+\b', str)
for word in words:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1
# 对结果进行排序
result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# 查看出现频率最多的前10个单词
print(result[:10])
# 输入单词能够得到单词的出现次数和频率
word = input('请输入单词：')
if word in dic:
    print(f'{word}出现的次数为{dic[word]},频率为{dic[word] / len(words)}')
else:
    print('单词不存在')