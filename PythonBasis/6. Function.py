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

