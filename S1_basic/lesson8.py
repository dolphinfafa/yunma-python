import random

# 作业1
# 统计一串字符串，每个字母出现的频率，忽略大小写，打印成一个字典

# 随机生成一段字符串
str = ''
for i in range(100):
    str += chr(random.randint(65, 90))
    str += chr(random.randint(97, 122))
    str += chr(random.randint(48, 57))
print(f'生成的字符串为：{str}')

# 统计字母频率
dict = {}
for i in str:
    if i.isalpha():
        i = i.lower()
        dict[i] = dict.get(i, 0) + 1

# 打印字典
for i in dict:
    print(f'字母 {i} 出现了 {dict[i]} 次')

# 作业2
# 利用字母和数字，随机生成10个8位密码
for i in range(10):
    password = ''
    for j in range(8):
        letter = random.choice([0, 1, 2])
        if letter == 0:
            password += chr(random.randint(65, 90))
        elif letter == 1:
            password += chr(random.randint(48, 57))
        else:
            password += chr(random.randint(97, 122))
    print(f'生成的密码为：{password}')

# 作业3
# 判断用户输入的是不是一个手机号码
# 手机号需要是数字1开头
# 手机号需要是11位长度
# 手机号需要是纯数字
phone = input('请输入一个手机号码：')
if phone.isdigit() and phone[0] == '1' and len(phone) == 11:
    print('输入的是一个手机号码')
else:
    print('输入的不是一个手机号码')
