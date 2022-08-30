from builtins import print as _print
from sys import _getframe

# 自定义print辅助函数，打印显示行号，方便以后观察
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} 行：'# 注此处需加参数 1。
    return _print(f"{s}", *arg, **kw)

# ===================================================================

# input 函数 （接受的输入转string）

# message = input("请随意输入(回车)~\n")
# print(message)

# name = input("请输入名字：")
# print(f"\nHello, {name.title()}!")

# 使用int() 来获取数值输入 （string 转 int）
# age = input("输入年龄：")
# age = int(age)
# if age >= 18:
#     print("成年了！")
# else:
#     print("乳臭未干~")

# 求模运算符 (% 两个数相除并返回余数)
print(4%3)
print(6%3)
print(7%4)

print("=================")

# 使用while 循环
num = 1
while num < 5:
    print(num)
    num += 1

msg = ''
while msg != 'quit':
    msg = input("请随意输入，输入(quit)退出。\n")
    if msg != 'quit':
        print(msg)

# 使用标记 (终止循环)
prompt = "请随意输入："
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# 使用break 退出循环
prompt = "break 请随意输入："
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)
    
# 在任何Python循环中都可使用break 语句。例如，可使用break 语句
# 来退出遍历列表或字典的for 循环。


# 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1 
    if current_number % 2 == 0:
        continue 
    print(current_number)

# 在列表之间移动元素
# 将 unconfirmed_users 用户移动到 confirmed_users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

print(confirmed_users == False) # False

# 当 unconfirmed_users = [] 是
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user) 

print(confirmed_users)


# 删除为特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat'] 
print(pets) 

while 'cat' in pets: 
    pets.remove('cat') 
 
print(pets)
