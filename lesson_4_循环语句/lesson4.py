# 输出99乘法表
# 使用while循环输出
def multiTable1():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print(f"{j} * {i} = {i * j}", end='\t')
            j += 1
        print()
        i += 1

# 使用for循环输出
def multiTable2():
    for i in range(1, 10):
        for j in range(1, i+1):
            print(f"{j} * {i} = {i * j}", end='\t')
        print()

if __name__ == '__main__':
    print("使用while循环输出99乘法表")
    multiTable1()
    print("使用for循环输出99乘法表")
    multiTable2()