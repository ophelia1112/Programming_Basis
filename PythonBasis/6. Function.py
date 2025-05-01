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


# 5. function and dict
students = {  
    'Tom' : {'id' : 101,'age' : 21,'height' : 189},
    'Lily' : {'id' : 102,'age' : 20,'height' : 178},
    'Alice' : {'id' : 103,'age' : 23,'height' : 190},
}

def get_student(name): 
    if name in students:
        return students[name] 
    else:
        return None

get_name = get_student('Tom')
print(get_name)


# 6. function and list
total = {
    'fruits' : ['apple','banana','orange'],
    'animals' : ['cat','dog','monkey'],
}
def get_information(something):
    if something in total:
        return total[something]
    else:
        return None

get_something1 = get_information('fruits')
get_something2 = get_information('animals')
print(get_something1,get_something2)



# practice
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


# 7. function import
import document: import documentname / import documentname.function1
import documentname as dc / from documentname import function1, function2 / from documentname import * (random)

# 8. lambda
the usage of lambda function is to define function directly
example: sum = lambda x,y:x+y 



# 列表排序方法：list.sort(key = None,reverse = False)   或者是  new_list = sorted(literable, key = None, reverse = False)
# 在列表排序函数中，有一个key参数，这个参数就可以传入一个函数，指定排序的元素，此时用lambda函数就可以简化代码，下方例子，对学生数据按照成绩排序
students_grades = [('xiaoming',89),('xiaoliu',90),('xiaozhang',78)]  #在这种情况下，用students_grades.sort()只会按照第一顺序排序
students_grades.sort(key = lambda x:x[1]) #x是我们要比较的项目，即将列表中的元组当成x（可以更改），而我们要比较的是第一项，即名字是第零项，成绩是第一项，这样就可以针对列表中的多个元组数据进行指定项的排序与其他函数的作用
new_list = sorted(students_grades, key = lambda x:x[1], reverse = True)
print(students_grades)
print(new_list)
# lambda函数本身是一个简化的写法，也可以用函数代替，只不过步骤较多



