# 函数：函数就是给一段代码起一个名字，可以独立的调用，可以重复使用这段代码，使用函数，就让程序的编写阅读升级更加容易
# 已经用过的函数，后面都是别人的代码，可以重复利用：random（技术模块，需要进行引入即import）,print,split,input,len
# 自我定义函数：自己也可以进行函数的撰写，自己重复利用分享他人，技术开源，定义函数的步骤如下：定义一个函数用关键字def开头，函数的名字是通过名字来定义和使用函数，需要有括号来放参数，同时和if,while,for一样需要冒号结尾，函数体里面可以运行多行代码
def print_hello():
    print('hello world')  #函数就是定义一个模块，模块下方有多个代码，调用函数可以直接运行多行代码
    print('hello')
print_hello()
def print_lloo():
    print('nihao')
print_lloo()

# 函数接收参数:给函数提供参数,做出不同反应,函数中的函数参数叫做形参,在函数里面可以使用,而且这个参数只能在函数里面使用,如下是例子
def introduce(name): #这里面的参数是函数参数,是形参,在函数里面使用,并且只能在函数里面使用
# 幼儿园的自我介绍
    print(f'大家好,我的名字是{name},我是一名幼稚园小同学')
# 调用函数,可以传递不同参数,多次调用
introduce('小明')  #参数赋值,调用函数传递真实数据参数,叫做实参
introduce('小红')  #提供参数实现不同控制
# 练习：类的模块的继承与不同模块的传递
def sum_numbers(number):  #定义函数
    # 计算1-number之间的和
    # :param number:数字
    # return:加和结果
    sum_value = 0  #初始的未加总的值
    for i in range(1,number + 1):  #  加总1到我们所输入的数字那就将所有数字遍历,同时保证输入数字在内即加一
        sum_value += i  #实现数字和
    print('number加和结果是:',sum_value)
sum_numbers(10)
# 重点在于遍历循环!!!!!!!
# 函数的调用参数,即函数怎样接收多个参数,即为函数提供参数,做出不同的反应
def introduce(name,gender): #逗号分隔,可以引入多个参数,
    print(f'大家好,我的名字是{name},我是一名{gender}')
introduce('小明','男生') #调用函数相应也应该该给予多个参数,但是要严格遵循顺序
# 函数关键字实参:使用key = value的形式,提供多个实参,顺序不太重要
def introduce(name,gender): # 参数较多,查找关键字参数,可以和上述的参数混合使用
    print(f'大家好,我的名字是{name},我是一名{gender}')
introduce(name = '小明',gender = '男生')
introduce(gender = '女生',name = '小红')
# 函数默认值参数:形参定义时,最后几个参数里,可以设置带默认值的参数
def introduce(name,gender,age = 6):  #其中年龄就是默认参数
    print(f'大家好,我的名字是{name},我是一名{gender},今年{age}岁')
    # 调用参数默认参数可以不写值,如果不设置年龄值,那就默认六岁
introduce('小明','男生')
introduce('小花','女生',5) #设置一个不同的值覆盖默认值

# 上述介绍的多种函数传递参数的方法,有位置实参按顺序,关键字参数用键等于值的方法,默认参数可以不填也可以填的方法调用,以上的调用都可以用
# 练习：类的模块的继承与不同模块的传递

def compute(x,y,method = 'add'):  #字符串类型注意引号

    if method == 'add':
        print('相加结果为:',x + y)
    elif method == 'sub':
        print('相减结果为:',x - y)
    elif method == 'mul':
        print('相乘结果为:',x * y)
    elif method == 'div':
        print('相除结果为:',x / y)
compute(x = 2,y = 7) #关键字实参是x,y,位置实参是2,7,这是有顺序的运算,已经规定了x,y
compute(y = 9,x = 6) #同理,顺序运算,也是没有更改默认计算方法的参数
compute(2,3,'div') # 数据参数,关键参数,这是无顺序运算,数字怎么排列计算都可以,但是更改了默认计算方法
compute(x = 3,y = 3,method = 'mul') #这是更改了默认计算方法的参数,同时规定了计算顺序
# 三种方式主要是实现对于数据的不同的控制,上文是只有两个数据,多个数据处理方法就不同了,例如下面的例子,实现所输入数字的从一到所输入数字与5的差

# 函数的返回值：函数可以具有一个或者是一组值，将整个函数逻辑封装在函数中，简化整个程序运行
# 函数返回单个值
def add(x,y):
#     变化输入数据类型，即将其他数据转化成为整数
    x = int(x)
    y = int(y)
# 函数的返回值即加上return即可
    return x + y

result = add(7,8)  #函数的赋值
print('两个值相加的结果是：',result)
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



