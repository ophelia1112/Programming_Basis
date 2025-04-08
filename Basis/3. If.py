# if入门：条件判断即使电脑根据不同的条件选择执行程序，示例代码：
grades = [60,70,99,89,34,56]
for grade in grades:
    print('你的成绩是：',grade)
    if grade >= 60: #条件测试
        print('恭喜你，通过考试')
    else:
        print('很遗憾，你没能通过考试，请继续努力')

# 更多类型的条件测试：条件判断都返回Ture或者False
# 字符串与数字比较运算符：a == b （等于）  a != b （不等于）  a > b （大于）  a >= b （大于等于）  a < b （小于）  a <= b （小于等于）
# a = b 是赋值， a == b 是判断a是否等于b
# 成员运算符: in:包含  not in:不包含
# 逻辑运算符：and:并且（条件同时满足才为真）  or:或者（条件之一也就是至少有一个满足则为真）  not a:非  可以加括号区分条件，and和or可以混合使用，但是先执行and后执行or，要改变这种优先级执行，用括号
# a == 3 and ('pear' not in fruits) or (value == 'ok')这里面先执行'a == 3 and ('pear' not in fruits)'再执行'('pear' not in fruits) or (value == 'ok')'
# 改变优先级即 a == 3 and (('pear' not in fruits) or (value == 'ok'))
# 在进行判断的时候，一般寻找数据，在print里面提前加上要判断的字符串，后续直接输出True或者False
# 练习：类的模块的继承与不同模块的传递
grade = 70
print('是否及格',grade >= 60)
print('是否不及格',grade < 60)
print('是否满分',grade == 100)
print('是否不是满分',grade != 100)
print('是否属于中等成绩',grade >= 70 and grade < 90)
print('成绩数字是否顺口',grade == 66 or grade == 88 or grade == 99)
print('成绩数字是否顺口',grade in list[66,88,99]) #前面已经有一个list，后面不得命名
print('成绩及格并且是否以零结尾',grade >= 60 and (grade == 60 or grade == 70 or grade == 80 or grade == 90 or grade == 100))
print('成绩及格并且是否以零结尾',grade >= 60 and grade in [60,70,80,90,100])
# if判断语句的语法
# 第一种：简单判断
grade = 70
if grade >= 60:
    print('你及格了')
# 配合else，表达如果否则含义
if grade >= 60:
    print('你及格了')
else:
    print('很遗憾不及格，继续努力')
# 配合多个elif和else，表达多个条件，只有一个条件会被执行
if grade <= 60:
    print('不及格')
elif grade < 80:  #else if 缩写
    print('良好')
elif grade <90:
    print('中等')
else:
    print('优秀')
# 只有一个条件会执行的现实应用易错点：网站用户名注册，判断用户名是否合法，即用户名至少要六个字符并且不能在已注册的列表里，多个条件测试，相互之间独立，独立if条件建立
users = ['xiaoming','xiaohua','xiaomei']
user_name = input('您输入的用户名为：')
if len(user_name) < 6:
    print('名字长度不足6，不可以注册')
if user_name in users:
    print('用户名在列表里，不可以注册')
# 练习：类的模块的继承与不同模块的传递
age = 20
if age <= 13:  #忘了加空格，可以格式化，即ctrl+alt+l
    print('小屁孩')
elif age >= 13 and age <= 18: #简化链式比较，Alt+Enter，变为13 <= age <=18
    print('青少年')
elif age >= 18 and age <= 65:
    print('成年人')
else:
    print('老年人')
# if判断和列表配合使用，例如判断列表中的奇数偶数
numbers = list(range(20))
for number in numbers:
    if number % 2 == 0:
        print('发现一个偶数：',number)
    else:
        print('发现一个奇数：',number)
# 判断用户注册
old_users = ['小明','小红','小东']
new_users = ['小明','小红','小李']
for new_user in new_users:
    if new_user in old_users:
        print('这个用户已经注册：',new_user)
    else:
        print('这个用户没有注册：',new_user)
# 练习：类的模块的继承与不同模块的传递：两数之和
numbers = [2,3,5,8,7,4,1,6]
aim_number = 8
for number1 in numbers:
    for number2 in numbers:
        if number1 + number2 == aim_number:
            print('这两个数相加等于8：',number1,number2) #但是是重复组合，3与5和5与3是一回事，这种情况排除重复组合？下方正式列表
            # print(f'{number1}和{number2}相加等于8')
# 创建一个空列表，用来存储已经配对过的数字，后期用并的关系排除重复项
# 值得深思的练习
result = []
numbers = [2,3,5,8,7,4,1,6]
aim_number = 8
for number1 in numbers:
    for number2 in numbers:
        if number1 + number2 == aim_number and (number1,number2) not in result:
            print('两个数相加等于8：',number1,number2)
            result.append((number1,number2))
            result.append((number2,number1)) #两对符合数对都在列表里，上面的判断条件只要保证数一数二不在列表里

