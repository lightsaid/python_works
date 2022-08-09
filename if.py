from builtins import print as _print
from sys import _getframe

# 自定义print辅助函数，打印显示行号，方便以后观察
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} 行：'# 注此处需加参数 1。
    return _print(f"{s}", *arg, **kw)

# ===================================================================

# 简单的示例 if elif else (语法没有 else if)  (而且可以独立与函数体)
cars = ["aa","bb","cc","dd"]
for car in cars:
    if car == "bb":
        print(f"这个{car}")
    elif car == "cc":
        print("哎呦~不错哟")
    else:
        print("什么玩意~")

# 比较符号 ==、!=、>、<、<=、>=
answer = 17 
if answer != 42: 
    print("17 != 42")

# and 检查多个条件
age_0 = 22
age_1 = 18
# print(age_0 >= 21 && age_1 >= 21)  # 居然不支持 && 语法
print(age_0 >= 21 and age_1 >= 21) # False
print(age_0 >= 21 or age_1 >= 21) # True

# in、not in 检查特定值是否包含在列表中
my_foods = ['pizza', 'falafel', 'carrot cake']
print("pizza" in my_foods) # True
print("pizza11" in my_foods) # False
print("pizza11" not in my_foods) # True

# 布尔表达式 （三元表达式）
car = 'subaru' 
### 不支持以下语法
# greet = car == 'subaru' ? '好车' : '辣鸡'
# print(greet)

# 这...
greet = "好车" if car == 'subaru' else "垃圾" 
print(greet) # 好车

# 就这？...
greet = ("好车", "辣鸡")[car == 'subaru']
print(greet) # 辣鸡 !!! 这操作666 第一个居然是false结果

# 确定列表不是空的
pizza_orders = ["aa","bb"]
# pizza_orders = []
if pizza_orders:
    for r in pizza_orders:
        print(f"制作批示{r}")
    print("制作完成")
else:
    print("百无聊赖,没事可做~")