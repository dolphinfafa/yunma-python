# homework 1
# 利用装饰器，记录程序运行次数
def run_times(func):
    def wrapper(*args, **kwargs):
        wrapper.run_times += 1
        print(f"程序运行次数：{wrapper.run_times}")
        return func(*args, **kwargs)
    wrapper.run_times = 0
    return wrapper

@run_times
def func():
    print("程序运行")

func()
func()

# homework 2
# 用r模式打开文件，如果文件不存在，则创建文件，如果文件存在，则读取文件内容
def open_file(file):
    try:
        with open(file, "r", encoding='utf-8') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        with open(file, "w", encoding='utf-8') as f:
            print("文件不存在，已创建文件")

open_file("test.txt")