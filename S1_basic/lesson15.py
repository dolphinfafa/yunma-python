# homework 1
# 批量生成12月份每天的txt文件，文件名为YYYY-MM-DD.txt
import datetime

def create_file():
    for i in range(1, 4):
        date = datetime.date(2024, 12, i)
        filename = date.strftime('%Y-%m-%d') + '.txt'
        with open(filename, 'w') as f:
            f.write('')
            f.close()

# homework 2
# 在上门生成的文件，写入文件名
def write_filename():
    for i in range(1, 4):
        date = datetime.date(2024, 12, i)
        filename = date.strftime('%Y-%m-%d') + '.txt'
        with open(filename, 'w') as f:
            f.write(filename)
            f.close()

# homework 3
# 在上门生成的文件名之后，加上'_NEW'

# homework 4
# 随机生成一个homework15.txt文件，里面内容为10行随机英文字母
# 读取homework15.txt文件，将里面大写字母变成小写字母，小写字母变成大写字母
import random

def homework15():
    with open('homework15_origin.txt', 'w') as f:
        for i in range(10):
            # 使用lamda表达式生成随机大小写字母
            str = [chr(random.randint(65, 90)) if random.randint(0, 1) == 0 else chr(random.randint(97, 122)) for i in range(10)]
            f.write(''.join(str) + '\n')
        f.close()

    with open('homework15_origin.txt', 'r') as f:
        content = f.read()
        f.close()

    with open('homework15_swap.txt', 'w') as f:
        f.write(content.swapcase())
        f.close()

create_file()
write_filename()
homework15()