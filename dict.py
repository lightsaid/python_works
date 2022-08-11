from builtins import print as _print
from sys import _getframe

# 自定义print辅助函数，打印显示行号，方便以后观察
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} 行：'# 注此处需加参数 1。
    return _print(f"{s}", *arg, **kw)

# ===================================================================

# 字典 (dict)
# 在Python中，字典 是一系列键值对 。每个键 都与一个值相关联，你可使用键来访问相关联的值.

alien_0 = {'color':'green', 'points': 5}
print(alien_0)
print(alien_0['color'])
# print(alien_0.color) 不支持点'.'语法

# 增加key/value
alien_0['x_pos'] = 0
alien_0['y_pos'] = 25

# 在Python 3.7中，字典中元素的排列顺序与定义时相同。
# 如果将字典打印出来或遍历其元素，将发现元素的排列顺序与添加顺序相同。

# 删除键值对
del alien_0['x_pos']
print(alien_0)

favorite_languages = {
    'jeb': 'python',
    'sarch': 'c',
    'wdware': 'ruby',
    'jack':'golang',
    'tom':'python'
}
print(favorite_languages)

# 使用 [] 取值, 如果不存在 key 则会报错
# print(favorite_languages['xqq'])

# Traceback (most recent call last):
#   File "/home/xzz/python_works/dict.py", line 39, in <module>
#     print(favorite_languages['xqq'])
# KeyError: 'xqq'


# 使用get(key, [defaultValue]) 来访问值, 避免key不存在报错
alien_0 = {'color':'green', 'points': 5}
print(alien_0.get('color')) # green
print(alien_0.get('x_pos')) # None
print(alien_0.get('x_pos', 0)) # 0

# 遍历所有键值对
user_0 = { 
    'username': 'efermi', 
    'first': 'enrico', 
    'last': 'fermi', 
}

# for key, value in user_0: { 错误语法, for 语句的第二部分包含字典名和方法items()
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue: {value}")

# 遍历 key (下面两种方式皆可以)
for k in user_0:
    print(k.title())

for k in user_0.keys():
    print(k.title())

# 大胆猜测,有没有直接遍历values的, 结果是有的
for v in user_0.values():
    print(v)

for key in user_0.keys():
    print(user_0[key])  # 在[]里使用变量是可以的, go语言不可以

# 对 key 临时排序遍历
favorite_languages = { 
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby', 
    'phil': 'python', 
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")


# set集合, 集合中的每个元素都必须是独一无二的
# 排除 favorite_languages 重复的 value 值
languages = set(favorite_languages.values())
print(languages) # {'c', 'python', 'ruby'}

# set 集合的创建, 使用 {}, 而 list 使用 [], 字典也是 {}
langs = {'python', 'ruby', 'python', 'c'}
print(langs)  # {'python', 'ruby', 'c'} 自动排除了重复数据

# 尝试在 set 里存重复的 dict 验证是否会去重
# 结果直接报错!!! TypeError: unhashable type: 'dict'
# alien_0 = {'color':'green', 'points': 5}
# alien_1 = {'color':'red', 'points': 10}
# alien_2 = {'color':'green', 'points': 5}
# aliens = {alien_0, alien_1, alien_2}
# print(aliens)

# 尝试在数组里存 dict, 是可以存的
alien_0 = {'color':'green', 'points': 5}
alien_1 = {'color':'red', 'points': 10}
alien_2 = {'color':'green', 'points': 5}
aliens = [alien_0, alien_1, alien_2]
print(aliens)

# 字典列表
# 快速创建
aliten_tpl = {'color':'green', 'points': 5}
aliens = [] 
[aliens.append(aliten_tpl) for i in range(30)]
print(aliens)

aliens_1 = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points': 5}
    aliens_1.append(new_alien) 
# 显示前5个外星人
for alien in aliens_1[:5]:
    print(alien)
print("OK....", len(aliens_1))

# 在字典中存储列表
pizza = { 
    'crust': 'thick', 
    'toppings': ['mushrooms', 'extra cheese'], 
}

print(pizza)

# 在字典中存储字典
users = { 
    'aeinstein': { 
        'first': 'albert', 
        'last': 'einstein', 
        'location': 'princeton', 
    }, 
    'mcurie': { 
        'first': 'marie', 
        'last': 'curie', 
        'location': 'paris', 
    }, 
}

print(users)