from builtins import print as _print
from sys import _getframe

# 自定义print辅助函数，打印显示行号，方便以后观察
def print(*arg, **kw):
    s = f'{_getframe(1).f_lineno} 行：'# 注此处需加参数 1。
    return _print(f"{s}", *arg, **kw)

# ===================================================================

def greet_user():
    """显示问候语"""  # 描述函数功能
    print("Hello, function.")

greet_user()
greet_user()

def greet_user(username):
    print(f"Hello, {username.title()}")

greet_user("lightsaid")
greet_user("lazy")


# 传递实参

def describe_pet(animal_type, pet_name):
    """显示宠物信息。"""
    print(f"\n I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('hamster', 'harry') 
describe_pet('dog', 'willie')


# 关键字实参 (调用函数时，明确指出各个实参对应的形参)
describe_pet(animal_type='hamster', pet_name='harry')

# 默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息。""" 
    print(f"\nI have a {animal_type}.") 
    print(f"My {animal_type}'s name is {pet_name.title()}.") 

describe_pet(pet_name='willie')


# 函数可返回任何类型的值，包括列表和字典等较复杂的数据结构

# 返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名。"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
 
musician = get_formatted_name('jimi', 'hendrix') 
print(musician)

# 返回字典
def build_person(first_name, last_name): 
    """返回一个字典，其中包含有关一个人的信息。""" 
    person = {'first': first_name, 'last': last_name} 
    return person 
 
musician = build_person('jimi', 'hendrix') 
print(musician)

# 传递列表
def greet_users(names):
    for name in names:
        msg=f"Hello, {name.title()}!"
        print(msg)

usernames = ['hahah','oo','aa']
greet_users(usernames)


### 在函数中修改列表 (列表是传递引用值)
### 将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修
### 改都是永久性的，这让你能够高效地处理大量数据。

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止。 
    打印每个设计后，都将其移到列表completed_models中。
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    for c in completed_models:
        print(c)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron'] 
completed_models = []
print_models(unprinted_designs, completed_models) 
show_completed_models(completed_models)


# 禁止函数修改列表
# 语法
# function_name(list_name_[:])

# 传递任意数量的实参（可变长参数）
def make_pizza(*toppings): # *toppings -> 元组
    """"打印顾客点的所有配料"""
    print(toppings)

 
make_pizza('pepperoni') 
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """"概述要制作的披萨"""
    print(f"要制作一个{size}寸披萨，所需材料如下：")
    for t in toppings:
        print(f"\t- {t}")

make_pizza(16, 'pepperoni') 
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')