from dog import *

# 使用 Python 标准库
from random import randint

dog1 = Dog('Whill', 6)
print(f"{dog1.name} - {dog1.age}")

dog1.site()
dog1.roll_over()

# 位于1和6之间的随机整数, 包括 1 和 6
print(randint(1, 6))