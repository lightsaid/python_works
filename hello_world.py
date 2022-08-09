from builtins import print as _print
from sys import _getframe

# 自定义print辅助函数，打印显示行号，方便以后观察
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} 行：'# 注此处需加参数 1。
    return _print(f"{s}", *arg, **kw)

# ===================================================================

# 打印
print("永远的 Hello World!")

# 变量定义
message = "永远的 Hello World~"
print(message)

message = "Python 速成班~"
print(message)

# 字符串 可以使用单引号/双引号/'''text'''
text = '''
这是一段话
这是一个段落
'''
print(text)

love = "love python"
print(love.title())

love = "Love Python"
print(love.upper())
print(love.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name.title())

print(f"Hello, {first_name.title()} {last_name.title()}")

message = f"Hello, {first_name} {last_name}"
print(message.title())

# \t \n
print("Languages:\tGolang\tJava\tPython\tJavaScript")
print("Languages:\nGolang\nJava\nPython\nJavaScript")

# strip
favorite_languages = 'python  '
print(len(favorite_languages))
print(len(favorite_languages.rstrip()))
# strip() rstrip() lstrip()


# 整数 +、 -、 *、 /、 ** 次方
print(3**2) # 9
print(3**3) # 27

print(0.1+0.2) # 0.30000000000000004

print(4/2) # 2.0 浮点数

# 数中下划线, 定义大数，方便阅读
universe_age = 14_000_000_000 
print(universe_age) # 14000000000

# 同时给多个变量赋值
x, y, z = 10, 20 ,30

# 常量: Python没有内置的常量类型，
# 但Python程序员会使用全大写来指出应将某个变量视为常量
MAX_AGE = 200
MAX_AGE = 300
print(MAX_AGE) # 300 程序中不做处理，仅仅程序员默认遵守规则

# 数字和字符串
message = "IPhone 14 Pro "
price = "2999.0"
print(message + price)

price = 2999.0
# print(message + price)  # 数字 不能和字符串相加
print(f"{message}{price}") # IPhone 14 Pro 2999.0 可以使用 f 函数

# Python 之禅
# >>> import this

# The Zen of Python, by Tim Peters

# Beautiful is better than ugly. 美观的比丑陋的好
# Explicit is better than implicit. 显式比隐式好
# Simple is better than complex.  简单胜于复杂。
# Complex is better than complicated.
# Flat is better than nested. 扁平比嵌套好。
# Sparse is better than dense. 稀疏胜于稠密。
# Readability counts. 可读性。
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
