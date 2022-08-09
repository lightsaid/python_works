from builtins import print as _print
from sys import _getframe

# 自定义print辅助函数，打印显示行号，方便以后观察
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} 行：'# 注此处需加参数 1。
    return _print(f"{s}", *arg, **kw)

# ===================================================================

# 定义 列表
bicycles = ["永久", "凤凰", "美利达", "喜德盛", "飞鸽"]
print(bicycles)

# 访问列表元素
print(bicycles[0])
# print(bicycles[5])  下表越界： list index out of range
print(bicycles[-1].title()) # 飞鸽

message = f"我家有一辆古老的{bicycles[1]}牌自行车。"
print(message)


### 修改、添加和删除元素
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = "ducati"
print(motorcycles)

# 追加 append
motorcycles.append("xx摩托车")
print(motorcycles)

# 插入 insert()
motorcycles.insert(10, "yy摩托车") # index 超出默认添加到末尾
print(motorcycles)

motorcycles.insert(1, "zz摩托车")
print(motorcycles)

# 删除 del 没返回值
del motorcycles[1]
print(motorcycles)

# 删除 pop() 弹出最后一个元素 （类似访问栈数据结构，last in fisrt out）
last = motorcycles.pop()
print(last)
print(motorcycles)

# 指定弹出(删除)哪一个
suzuki = motorcycles.pop(2)
print(suzuki)
print(motorcycles)
print(f"我想买{suzuki}这辆摩托车~")

# remove 根据值删除元素 （没返回值）
# 方法remove() 只删除第一个指定的值。如果要删除的值可能在列表中
# 出现多次，就需要使用循环来确保将每个值都删除。
_xx = "xx摩托车"
motorcycles.remove(_xx)
print(f"{_xx} 被移除了")
print(motorcycles)


# 组织列表

# 使用方法sort() 对列表永久排序
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() 
print(cars)
# 反序
cars.sort(reverse=True)
print(cars)

# sorted() [reverse=True] 临时排序 !!! sorted 不属于 list 方法
cars = ['bmw', 'audi', 'toyota', 'subaru']
temp_sort = sorted(cars)
print(temp_sort)
print(cars)

# reverse() list 反转 （非排序）
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# len() 获取列表长度
motorcycles = ['honda', 'yamaha', 'suzuki']
print(len(motorcycles))

# 获取最后一个元素，建议使用 list[-1] 而不是 list[len(list)-1]
motorcycles = []
# print(motorcycles[-1])  # 没有元素时，index会越界

# 遍历整个列表
magices = ["魔术师1号","魔术师2号","魔术师3号","魔术师4号"]
for m in magices: # : 冒号不能遗漏，循环体需要缩进
    print(m)

# 使用 range() 函数 生成一系列数值 区分（1个参数、2个参数、3个参数区别）

for vlaue in range (1, 5): # 生成的数不包含5
    print(vlaue)

for val in range(6): # 相当于 range(0, 6)
    print(val)

# range() 指定第三个参数(步长)
# list(range(2,11,2)) 从2开始数，然后不断加2，直到达到或超过终值11
even_numbers = list(range(2,11,2))
print(even_numbers)

# 创建（1~10）的平方
squares = []
for val in range(1,11):
    squares.append(val ** 2)

print(squares)

# 数字统计计算 函数 min() max()
print(min(squares))
print(max(squares))

# 列表解析 [表达式 for val in range(x,y)]
squares = [val**2 for val in range(10,21)]
print(squares)

# 动手试试（练习）

# 练习4-3：数到20 　使用一个for 循环打印数1～20（含）。
for num in [n for n in range(1,21)]:
    print(num)

# 练习4-4：一百万 　创建一个包含数1～1 000 000的列表，再使用一个for 循
# 环将这些数打印出来。（如果输出的时间太长，按Ctrl + C停止输出或关闭输
# 出窗口。）
# max_size = 1_000_000
# for num in [n for n in range(1, max_size)]:
#     print(num)

# 练习4-5：一百万求和 　创建一个包含数1～1 000 000的列表，再使用min()
# 和max() 核实该列表确实是从1开始、到1 000 000结束的。另外，对这个列表
# 调用函数sum() ，看看Python将一百万个数相加需要多长时间。
max_size = 1_000_000
sizes = [n for n in range(1, max_size)]
print(min(sizes))
print(max(sizes))
print(sum(sizes))  # 速度惊人

# 练习4-6：奇数 　通过给函数range() 指定第三个参数来创建一个列表，其中
# 包含1～20的奇数，再使用一个for 循环将这些数打印出来。
for num in [n for n in range(1, 20, 2)]:
    print(num) 

# 练习4-7：3的倍数 　创建一个列表，其中包含3～30能被3整除的数，再使用一
# 个for 循环将这个列表中的数打印出来。
for num in [n for n in range(3, 31, 3)]:
    print(num)

# 练习4-8：立方 　将同一个数乘三次称为立方 。例如，在Python中，2的立方
# 用2**3 表示。请创建一个列表，其中包含前10个整数（1～10）的立方，再使
# 用一个for 循环将这些立方数打印出来。
for num in [n**3 for n in range(1, 11)]:
    print(num)

# 练习4-9：立方解析 　使用列表解析生成一个列表，其中包含前10个整数的立方。
for num in [n**3 for n in range(1, 11)]:
    print(num)



### 使用列表的一部分 Slice
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[0:3][1:2]) # 遵循左闭右开
print(players[:2])
print(players[:-1]) # 从0开始到倒数第2个（排除最后一个）
print(players[-2:]) # 最后2个

# 复制列表 [:]
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods[0] = "披萨" # 不会影响到 my_foods
print(friend_foods)


## 元组 (不可修改的列表，但不是列表)
# Python将不能修改的值称为不可变的 ，而不可变的列表被称为元组 。

# 定义元组 使用()括号定义
dimensions = (200, 50) 
print(dimensions[0]) 
print(dimensions[1])
# dimensions[0] = 250 # TypeError: 'tuple' object does not support item assignment

# 严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更
# 清晰。如果你要定义只包含一个元素的元组，必须在这个元素后面加上逗号。
my_t = (3,)

# 修改元组变量（覆盖） 给元组变量重新赋值是合法
dimensions = (200, 50)
print(dimensions)
dimensions = (200, 50, 100)
print(dimensions)

