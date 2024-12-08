# 定义一个类：银行账户，可以做创建账户，存款，取款，查询余额，销户操作
import random

# 定义一个字典，存储账户信息
accounts = {}

class BankAccount:
    def __init__(self, phone, name, password, balance):
        # id为随机8位数字
        self.id = random.randint(10000000, 99999999)
        self.phone = phone
        self.name = name
        self.password = password
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("余额不足")
        else:
            self.balance -= amount

    def query(self):
        print("账户余额为：", self.balance)

    def __del__(self):
        print("账户已销户")

# 定义创建银行账户方法，并把账户信息存储到字典中
def create_account(accounts, phone, name, password, balance):
    # 判断手机号是否已经注册
    for account in accounts.values():
        if account.phone == phone:
            print("手机号已经注册")
            return 1
    # 判断手机号是否是1开头，并且是11位数字
    if not phone.startswith("1") or len(phone) != 11:
        print("手机号格式错误")
        return 2
    account = BankAccount(phone, name, password, balance)
    accounts[account.id] = account
    print("账户创建成功，账户id为：", account.id)
    return 0

# 定义一个函数：创建初始界面，选择操作
def main():
    # 选择操作
    while True:
        print("欢迎使用银行账户管理系统")
        print("1. 创建账户")
        print("2. 登录账户")
        print("3. 退出")
        choice = int(input("请选择操作："))
        if choice == 1:
            phone = input("请输入手机号：")
            name = input("请输入姓名：")
            password = input("请输入密码：")
            balance = float(input("请输入初始存款："))
            # 调用创建账户方法，
            # 如果返回值为1，手机号已经注册，重新输入手机号
            # 如果返回值为2，手机号格式错误，重新输入手机号
            # 如果返回值为0，账户创建成功
            if create_account(accounts, phone, name, password, balance) == 1:
                continue
            elif create_account(accounts, phone, name, password, balance) == 2:
                continue
            else:
                continue
        elif choice == 2:
            phone = input("请输入手机号：")
            password = input("请输入密码：")
            for account in accounts.values():
                if account.phone == phone and account.password == password:
                    print("登录成功")
                    print("1. 存款")
                    print("2. 取款")
                    print("3. 查询余额")
                    print("4. 销户")
                    print("5. 退出")
                    while True:
                        print("1. 存款")
                        print("2. 取款")
                        print("3. 查询余额")
                        print("4. 销户")
                        print("5. 退出")
                        choice = int(input("请选择操作："))
                        
                        if choice == 1:
                            amount = float(input("请输入存款金额："))
                            account.deposit(amount)
                            account.query()
                        elif choice == 2:
                            amount = float(input("请输入取款金额："))
                            account.withdraw(amount)
                            account.query()
                        elif choice == 3:
                            account.query()
                        elif choice == 4:
                            del account
                            break
                        elif choice == 5:
                            break
                        else:
                            print("请选择正确操作")
                else:
                    print("手机号或密码错误")
        elif choice == 3:
            break
        else:
            print("请选择正确操作")
            
if __name__ == "__main__":
    main()
