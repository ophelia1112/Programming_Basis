# 1. simple function
def print_hello():
    print('hello world') 
    print('hello')
print_hello()

# 2. parameters of function
def sum_numbers(number): 
    sum_value = 0 
    for i in range(1,number + 1):
        sum_value += i 
    print('The sum of numbers is :',sum_value)
sum_numbers(10)
# multiple paremeters need follow the order

# 3. default parameters
def introduce(name,gender,age = 6): 
    print(f'my name is {name}, I'm a {gender}, and I'm {age} years old.')
introduce('Tom','boy')
introduce('Lily','girl',5)

# 4. return
def add(x,y):
    x = int(x)
    y = int(y)
    return x + y
result = add(7,8)  
print(result)


# 函数返回字典
students = {  #学生信息汇总
    'xiaoli' : {'id' : 101,'age' : 21,'height' : 189},
    'xiaohua' : {'id' : 102,'age' : 20,'height' : 178},
    'xiaozhang' : {'id' : 103,'age' : 23,'height' : 190},
}

def get_student(name):  #此函数的目的就是让使用者输入函数调用相对应的字典数据
    if name in students:
        return students[name]  #输入名字即调用数据
    else:
        return None

get_name = get_student('xiaoli')
print(get_name)
print(get_student('xiaozhang'))


# 函数返回列表
total = {
    'fruit' : ['apple','banana','orange'],
    'animal' : ['cat','dog','monkey'],
}
def get_information(something):
    if something in total:
        return total[something]
    else:
        return None

get_something1 = get_information('fruit')
get_something2 = get_information('animal')
print(get_something1,get_something2)


# 函数可以返回多个值，调用的时候可以进行拆分处理，其实是返回了一个元组数据对象，即函数返回元组
students = {
    'xiaoli' : {'id' : 101,'age' : 21,'height' : 176},
    'xiaohua' : {'id' : 102,'age' : 23,'height' : 189},
    'xiaoliu' : {'id' : 103,'age' : 24,'height' : 179},
}

def get_students(name):
    if name in students:
        return students[name]['age'],students[name]['height']
    else:
        None,None  #返回多个值，也要对应返回多个None，有几个值返回几个None，一一对应
age,height = get_students('xiaohua') #分开变量接收
stock = get_students('xiaohua')
print(age,height,stock) #stock就是元组对象的接收

# 练习：类的模块的继承与不同模块的传递
def compute(x,y,method):
    if method == 'add':
        return x + y
    elif method == 'sub':
        return x - y
    elif method == 'mul':
        return x * y
    elif method == 'div':
        return x / y
    else:
        return None
print(compute(2,33,'add'))

def add(x,y):
    return x + y
# 或者是return compute(x,y,'add'),在这一步就是直接返回了一个底层函数compute，方便调用，下文同理
print(add(2,4))
def sub(x,y):
    return compute(x,y,'sub')
print(sub(6,4))

# 将函数储存在模块中，在实际的开发过程中，代码都是存在于不同的文件之中，而python的代码文件就是以.py为后缀结尾的文件，这也就是模块，通过python中的import语句，引入一个函数即代码模块进行使用
# 例如新建一个compute函数即模块，compute.py，在模块里编写add,sub,mul,div四个函数，所以compute就是一个模块，这个模块里面的四个函数也可以在其他的文件中进行调取使用
# 即当我们新建一个以.py为后缀的文件时，我们可以调用事先编写好的函数及其模块，即import compute，在用compute模块调用它里面的函数，即compute.add，用函数进行相应的计算操作
# 当然也有不同的调用方法，即import compute as cp: 这就是给调用的模块起了一个名字即cp，再用重新的命名来直接调用函数，为了简化代码书写
# 也可以直接引用函数使用，from compute import add,sub直接使用加减函数，from compute import *: 可以直接随机引入函数（一般不用星）
# 进行实例的文件为compute.py 与 main.py
# 函数存储模块练习题：student_query.py 与 school.py


# lambda函数和列表顺序
# 在编程之中有一个特殊的函数即lambda函数，又称为匿名函数，函数的定义直接使用，不用起名字，函数逻辑简单，一行代码就能实现表达逻辑，多用于一些简单的不重复多次调用的场景
# 定义的形式：lambda 参数：操作（参数）  举例：sum = lambda x,y:x+y 就可以使用sum函数进行加法运算了
# 之所以将一行逻辑写成一个函数是因为在编程里有高级函数的调用需要传一个函数作为参数传入，即有些复杂函数中的参数，我们可以传一个函数进去，而这个函数写的越简单越好，进而传给复杂函数本身，即将底层逻辑用lambda编写，传入给复杂函数，这也是对函数即编程的理解
# 例证：列表排序函数和lambda函数
# 列表排序方法：list.sort(key = None,reverse = False)   或者是  new_list = sorted(literable, key = None, reverse = False)
# 在列表排序函数中，有一个key参数，这个参数就可以传入一个函数，指定排序的元素，此时用lambda函数就可以简化代码，下方例子，对学生数据按照成绩排序
students_grades = [('xiaoming',89),('xiaoliu',90),('xiaozhang',78)]  #在这种情况下，用students_grades.sort()只会按照第一顺序排序
students_grades.sort(key = lambda x:x[1]) #x是我们要比较的项目，即将列表中的元组当成x（可以更改），而我们要比较的是第一项，即名字是第零项，成绩是第一项，这样就可以针对列表中的多个元组数据进行指定项的排序与其他函数的作用
new_list = sorted(students_grades, key = lambda x:x[1], reverse = True)
print(students_grades)
print(new_list)
# lambda函数本身是一个简化的写法，也可以用函数代替，只不过步骤较多



