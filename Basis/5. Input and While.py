# input函数可以实现用户输入，input(message)函数可以给用户提示信息，等待用户输入，进行处理
# 注意的点就是，input(message)函数有只返回字符串，要进行数值计算就要转换int类型
number = input('输入一个数字，就要给你计算他的平方：')
number = int(number)  #转换数据类型
print(f'您输入的数字为{number},他的平方是{number * number}')
# 练习题
number = input('请输入一个数字：')
number = int(number)
if number % 2 == 0:
    print(f'您输入的数字是{number},是一个偶数')
else:
    print(f'您输入的数字为{number},是一个奇数')
# while循环与input的配合使用：while和for一样都是循环控制语法，for ... in ...的语法结构，方便针对集合中的元素进行遍历处理，而while则会指定一个条件，不满足就退出循环
# 练习：类的模块的继承与不同模块的传递：计算1-100数字和，语法
number,sum_value = 1,0  #多个变量的呃巧利用
while number <= 100:  #满足条件一直循环，不满足就输出循环结果
    sum_value += number
    number += 1  #防止死循环，但是也有死循环，例如用户一直在玩游戏，一直循环
print(sum_value)
# while循环直到条件结束：对于while与for循环，用break退出循环，用continue直接跳到下一次循环，也就是break跳出for/while的整体循环，继续向下执行代码，continue是结束for/while的当次本次循环，继续下一个循环
# while循环与input实现不断的交互直到结束
while True:
    print('#'*10) #分隔符
    fruit = input('请输入您喜欢的水果，输入quit会退出循环：')
    if fruit == 'quit':
        break
    else:
        print(f'很好你喜欢的水果为{fruit}')
# 几个例子
# input与while实现快递运费程序
while True:
    print('#' * 20)  #分隔符
    weight = input('请输入您的商品重量（kg），输入quit退出计算价格：')
    if weight == 'quit':
        break
    else:
        weight = float(weight)  #重量用浮点数既包括小数也包括整数
        if weight <= 0:
            print('您输入的有误')
            continue
        if weight < 1:
            print('金额是7元')
        elif 1 < weight < 3:
            price = 7 + 2 * weight
            print(price)  # print(‘金额是’,7 + 2 * weight),下方同理
        elif weight >= 3:
            price = 7 + 3 * weight
            print(price)
        else:
            print('输入错误，你输入的是：',weight)

# while循环将数据存储到列表：while循环不只可以单次处理，它本身就是循环反复，实现列表元素的处理，如从互联网的网页上爬取数据，即爬虫，while可以实现列表字典等多种数据的处理
import time  #爬取一个新的模块
web_todo = ['web1','web2','web3']  #等待爬取的网站
web_success = []  #已经爬取成功的网站

while web_todo:
    new_web = web_todo.pop() #爬一个删除一个
    print('正在爬取web:',new_web)
    time.sleep(1)  #暂停5秒钟，模拟爬取
    web_success.append(new_web) #记录爬取过的数据

print('爬取完毕：',web_success)
print('待爬取：',web_todo)
# while循环将数据存储到字典，存储到字典里面方便处理数据
student_grades = {}
while True:
    stock = input('请输入学生的姓名与成绩，中间用空格分割：')
    if stock == 'quit':
        break
    name, grade = stock.split()
    grade = int(grade)
    student_grades[name] = grade
print('学生信息如下：')
for name,grade in student_grades.items():
    print(name,grade)

print('学生成绩最高分是：',max(student_grades.values()))
print('学生成绩的最低分是：',min(student_grades.values()))
print('学生成绩的平均分是：',sum(student_grades.values())/len(student_grades))

# while与input配合完成练习题：猜字游戏
# 猜字游戏：使用random.randint(1,100)随机生成一个数字target，循环十次，让用户猜数字
# 用户猜的数字比target大，提示用户猜大了，继续循环猜测
# 如果用户猜的数字比target小，提示用户猜小了，继续循环猜测
# 如果用户猜出来的数字正好是target，提示恭喜用户猜对了，退出循环
# 如果猜了十次还没猜对，
# 新知识：import random
import random
target = random.randint(1,100)
# print(target)  自己都不知道随机数是哪个才好玩
success = False  #没有成功是错的
time = 0
while time <= 10:
    number = input('请输入您猜测的数字：')
    if not str(number).isnumeric():  #判断数字
        print('输入的不是数字，请重新输入')
        continue
    number = int(number) #上方是整数类型，整数之间做比较
    if number == target:
        print('恭喜你猜对了')
        success = True  #成功以后是正确的
        break
    elif number < target:
        print(f'您输入的数字是{number}，猜的小了')
    else:
        print(f'您输入的数字是{number}，猜的大了')
    time += 1
else:
    print(f'很遗憾你没猜对，正确答案是{target}')

if not success:
    print('再接再厉')

# 如果输入的不是数字，怎么办？这就需要插入一些帮助代码更加完善的内容

