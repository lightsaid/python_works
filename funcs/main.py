# 导入整个模块

# 让Python打开文件foo.py，并将
# 其中的所有函数都复制到这个程序中。
import foo

# 导入模块中的所有函数
# import 语句中的星号让Python将模块pizza 中的每个函数都复制到这个程序文件中。
from bar import *

# foo_module() name 'foo_module' is not defined. Did you mean: 'bar_module'
foo.foo_module()

bar_module()


# 导入特定的函数 语法：（module_name -> module_name.py）
# from module_name import function_name 
# from module_name import function_0, function_1, function_2


# 使用 as 给函数指定别名 语法：
# from pizza import make_pizza as mp 
# 使用 pizza 模块函数
# mp(16, 'pepperoni') 
# mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# 使用 as 给模块指定别名 语法：
# import pizza as p 
# p.make_pizza(16, 'pepperoni') 
# p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese') 