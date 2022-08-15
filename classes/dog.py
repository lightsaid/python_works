class Dog:
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def site(self):
        """模拟小狗收到命令时蹲下。""" 
        print(f"{self.name} is now sitting.")

    def roll_over(self): 
        """模拟小狗收到命令时打滚。""" 
        print(f"{self.name} rolled over!")

dog1 = Dog('Whill', 6)
print(f"{dog1.name} - {dog1.age}")

dog1.site()
dog1.roll_over()