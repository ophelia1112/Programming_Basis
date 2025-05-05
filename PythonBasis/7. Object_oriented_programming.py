# 1. class(property and method)
class Student: 
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def introduce(self):
        return f'大家好。我叫{self.name},我今年{self.age}岁了'

xiaoming = Student('小明',18) 
xiaozhang = Student('小张',17)
xiaozhao = Student('小赵',19)
print(xiaoming.name,xiaoming.age,xiaoming.introduce())
print(xiaozhang.name,xiaozhang.age,xiaozhang.introduce())
print(xiaozhao.name,xiaozhao.age,xiaozhao.introduce())

class Phone:
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def describe(self):
        return f'这是{self.model}手机，价格是{self.price}'
    def call_friend(self,friend_name):
        return f'我在用手机{self.model}打电话给{friend_name}' #再加一个self防止变红

iphone13 = Phone('苹果13',6000)
huaweip50 = Phone('华为P50',4000)



print(iphone13.model,iphone13.price,iphone13.describe(),iphone13.call_friend('小李'))
print(huaweip50.model,huaweip50.price,huaweip50.describe(),huaweip50.call_friend('黎明'))

# 修改类的对象的属性
class StudentGrades:
    def __init__(self,name,yuwen,shuxue):  #三个属性
        self.name = name
        self.yuwen = yuwen
        self.shuxue = shuxue
    def update(self,course,grade): #普通更新函数，构造函数进行值的修改
        if course == 'yuwen':
            self.yuwen = grade
        elif course == 'shuxue':
            self.shuxue = grade
xiaoming = StudentGrades('小明',88,99)
xiaoming.yuwen = 89 #修改属性值，用.直接访问属性本身进行修改
xiaoming.shuxue = 96
print(xiaoming.yuwen,xiaoming.shuxue)
xiaoming.update('语文',88) #也可以借助函数，即update
xiaoming.update('数学',96)
print(xiaoming.yuwen,xiaoming.shuxue) #打印的时候直接命名加属性就可以访问

# 类的对象可以放在列表和字典里
xiaoming = StudentGrades('小明',88,99) #对应上方代码的语文成绩与数学成绩
xiaozhang = StudentGrades('小张',87,93)
xiaozhao = StudentGrades('小赵',88,90)

student_list = [xiaoming,xiaozhang,xiaozhao]
for student in student_list:
    print(student.name,student.yuwen,student.shuxue)
student_dict = {'小明':xiaoming,
                '小张':xiaozhang,
                '小赵':xiaozhao
                }
for name,student in student_dict.items():
    print(f'学生{name}的成绩是{student.yuwen},{student.shuxue}')

# 练习题：婚礼礼金,类与列表
class Customer:  #注意缩进，类分开搞
    def __init__(self,name,money):
        self.name = name
        self.money = money


customers = []
moneys = []
while True:
    info = input('请输入您的姓名与礼金数额，输入quit结束程序：')
    if info == 'quit':
        break
    name,money = info.split()
    money = int(money)
    # customer = Customer(name,money)
    # customers.append(customer)
    customers.append(Customer(name,money))
    moneys.append(money)
print('访客总人数：',len(customers),   '总金额：',sum(moneys),    '最大金额：',max(moneys),    '最小金额：',min(moneys),   '平均金额:',sum(moneys)/len(moneys))

# 面向对象的继承（理解，python更注重函数编程）
# 即类的继承，现实中有一些这样的关系，汽车分为不同的型号价格行驶里程，其中油车电车油电混动的车都各自有不同的特性，但是把三种车所涉及的所有代码都放在一个类代码里面太庞大，三种汽车都实现一遍型号价格行驶里程的公共属性方法太过冗杂，也就有了以下的类的继承
# 面向对象存在一个机制叫做继承，首先定义父类如car，提供所有公共属性方法，即型号价格行驶里程，每个车根据自身所具备的特殊的属性以及方法进行不同的操作
# 代码示例
class Car:
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def info(self):
        print(f'车型是{self.model},价格是{self.price}万元')

# 下方是子类对象self油车A，子类对象self油车B,嵌入的是父类对象car
class Oilcar(Car): #继承父类
    def __init__(self,model,price,box_size): #有了油箱的个人属性
        super().__init__(model,price) #super是父类对象，所以用super函数初始化调用父类的属性，调用时候需要初始化父类的某块区域
        self.box_size = box_size

    def add_oil(self,money):
        print(f'老板，加{money}元的油')
    def info(self): #info函数是覆盖方法
        super().info()
        print('我是油车，跑起来比电动车动力更足')
car01 = Oilcar('路虎',60,50)
print(car01.model,car01.price,car01.box_size)
car01.info()  #info加上print本身没有访问值，直接访问就可以，不用加上print，不然就出现none
car01.add_oil(200)


class ElectricCar(Car):
    def __init__(self,model,price,battery_size):
        super().__init__(model,price)
        self.battery_size = battery_size

    def add_electric(self,money):
        print(f'车价值{self.price},充电花了{money}元') #price来自于本身的父类属性
    def info(self):
        super().info()
        print('我是电车更省钱')

car02 = ElectricCar('特斯拉',200,100)
print(car02.model,car02.price,car02.battery_size)
car02.info()
car02.add_electric(90)

# 类的继承机制练习题
class User: #父类
    def __init__(self,name,passward):
        self.name = name
        self.passward = passward
    def welcome(self): #初始语句，后面可能进行覆盖
        print(f'你好{self.name}，欢迎你的到来')

class Admin(User): #超级管理员
    def __init__(self,name,passward): #无新属性增加
        super().__init__(name,passward)
    def welcome(self): #覆盖父类的提示语
        print(f'你好尊贵的管理员{self.name}，欢迎你的到来')
    def manage(self): #方法
        print(f'管理员{self.name},您正处于管理系统')


class Vip(User):
    def __init__(self,name,passward,money): #增加了新属性钱
        super().__init__(name,passward)
        self.money = money #新属性定义一下
    def welcome(self): #覆盖父类提示语
        print(f'您好，尊贵的VIP用户{self.name}，欢迎归来')
    def vip_service(self): #方法
        print(f'你好，尊贵的VIP{self.name}，给你提供贵宾服务')

# 以下为用户的属性输出以及方法调用
admin01 = Admin('圆圆',908903)
print(admin01.name,admin01.passward)
admin01.welcome()
admin01.manage()
admin02 = Admin('龙龙',8989319)
print(admin02.name,admin02.passward)
admin02.welcome()
admin02.manage()
vip01 = Vip('大艺',38292,300)
print(vip01.name,vip01.passward,vip01.money)
vip01.welcome()
vip01.vip_service()
vip02 = Vip('慧慧',90901,400)
print(vip02.name,vip02.passward,vip02.money)
vip02.welcome()
vip02.vip_service()
user01 = User('金刚',717391)
user01.welcome()
user02 = User('哇哇',902031)
user02.welcome()
# 用处：网站开发输入

# 将类写在不同的模块中：将类写在文件模块中
class Car:
    def __init__(self,model,price):
        self.model = model
        self.price = price

    def info(self): #方法
        print(f'车子的型号是{self.model},价钱是{self.price}')

# 下方是几种引入另一个文件中的类的方法，其实就是和函数一样，构造car.py文件与调用文件
import car
my_car = car.Car('路虎', 80) #上文代码
my_car.info() #直接调用

import car as c
my_car = c.Car('路虎',80)
my_car.info()

from car import Car
my_car = Car('路虎',80)
my_car.info()

from car import *
my_car = car.Car('路虎', 80)
my_car.info()

# 练习题文件：animal,sheep,tiger,all animal


