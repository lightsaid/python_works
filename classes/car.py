class Car:
    """一次模拟汽车的简单尝试."""
    def __init__(self, make, model, year):
        """初始化汽车属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # 里程表, 在 __init__ 方法里没有定义此形参

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息."""
        print(f"This car has {self.odometer_reading} ....")

    def update_odometer(self, mileage): 
        """将里程表读数设置为指定的值, 禁止将里程表读数往回调。""" 
        if mileage >= self.odometer_reading: 
            self.odometer_reading = mileage 
        else: 
            print("You can't roll back an odometer!")
    def talking(self):
        print(f"{self.model} 是汽油车....")

car1 = Car('audi', 'a4', 2019)
print(car1.get_descriptive_name())
car1.read_odometer()
print(car1.odometer_reading)

car1.odometer_reading = 10
print(car1.odometer_reading)

car1.update_odometer(22)
car1.read_odometer()

car1.update_odometer(20) # You can't roll back an odometer!
car1.read_odometer()

# 刹车 class
class Brake:
    """一次刹车的尝试"""
    def __init__(self, is_barrier=False, distance=0):
        self.is_barrier = is_barrier # 是否有障碍物
        self.distance = distance # 距离多少米

    def brakeing(self):
        if(self.is_barrier and self.distance < 50):
            print("采取自动刹车措施...")
        else:
            print("正常行驶中...")

# 继承 
# 语法
# class children(parent):
#     def __init__(self, xx, yy, ...):
#         super().__init__(xx, yy, ...) 

class ElectricCar(Car):
    """电动汽车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类属性"""
        super().__init__(make, model, year)

        # 特有的属性(电瓶容量)
        self.battery_size = 75

        # 将实例作为属性
        self.brake = Brake()

    def describe_battery_size(self):
        print(f"容量是 {self.battery_size}")

    # 重写父类
    def talking(self):
        print(f"{self.model} 是新时代电车....")

    

car2 = ElectricCar("tesla", "model", 2019)
print(car2.get_descriptive_name())
car2.describe_battery_size()

# : 'Car' object has no attribute 'describe_battery_size'
# car1 是 Car 的实例，没有 describe_battery_size 方法
# car1.describe_battery_size()

car2.talking()

# 测试 brake 属性
car2.brake.brakeing()

car2.brake.is_barrier = True
car2.brake.distance = False
car2.brake.brakeing()