# 1. List
animals = ['cat','dog','chicken']
print(animals)
print(type(animals))


# 2. Get elements in list
# Indexing method
print(animals[0])
print(animals[-1])



# 列表的操作：新增，删除，修改，修改是list[下标] = 新值，新增列表值是通过append()函数，即list.append(元素)，给末尾添加元素，删除元素是通过remove()函数,即list.remove(元素)
new_list[0] = 'pear'
print(new_list)
new_list.append('oranges')
print(new_list)  #一般是初始化一个空列表，逐步增加数据
new_list.remove('pear')
print(new_list)
# 练习：类的模块的继承与不同模块的传递
guests = ['小张','小王','小李']
guests.remove('小王')
guests.append('小黄')
print(guests)
# 列表排序与长度：列表的排序用list.sort()，一般默认升序，加上reverse = Ture，实现倒序，即降序
grades = [11,89,45,67,87,34]
grades.sort()
print(grades)
grades.sort(reverse=True)
print(grades)
# 上述的方法将原列表改动了，如果不想原列表被改变并且持续输出修改以后列表，用sorted(list)方法，不会修改原来列表，并且返回一个新排序列表
grades1 = sorted(grades)
print(grades,grades1)
grades2 = sorted(grades,reverse=True)
print(grades,grades2)
# 洞察列表长度，用len()函数
print('成绩的个数为：',len(grades))
# 列表list和循环loop
# 循环打印列表元素：for循环遍历与while循环遍历,
list1 = ['lili','lolo','lilei']
for i in list1:  #这里面的i只是遍历的变量名，可以更改
    print(i)  #可以打印多行。例如下文
for name in list1:
    print(f'我的名字是{name}')
    print(f'我之所以叫{name},是因为是妈妈起的')
    print(name)
# 使用range生成数字列表：使用range遍历数据，range函数即range(start,stop,step)，其中start包含数字，stop不包含数字，step是步长，即间隔数字，range（5），即01234
for number in range(1,21):
    print(number)
# range是一个类型，进行转换
# print(type(range(1,21)))
# print(range(1,21))
#
# data = list(range(1,21))
# print(data,type(data))

# 列表简单统计计算
# max(list)：返回列表最大值
# min(list)：返回列表最小值
# sum(list)：返回列表值加和
# len(list)：返回列表元素个数
data = [1,2,3,4,5,6,7,8]
print('列表最大值为',max(data))
print('列表最小值为',min(data))
print('列表总和为',sum(data))
print('列表元素个数为',len(data))

# numbers = list(range(0,100))
# print('列表最大值为',max(numbers))
# print('列表最小值为',min(numbers))
# print('列表总和为',sum(numbers))
# print('列表元素个数为',len(numbers))

# 列表推导式（简化）：使用for循环，使用现在的序列或者列表生成一个新的列表
# 生成1-100所有数字平方的列表
numbers = [i*i for i in range(1,101)]
print(numbers)
# 生成1-100所有偶数平方列表
numbers = [i*i for i in range(1,101) if i % 2 == 0] #整出为零就是偶数，后面加条件直接加
print(numbers)
# 生成1-100所有奇数平方列表
numbers = [i*i for i in range(1,101) if i % 2 ==1] #  %是取余
print(numbers)
numbers = [i for i in range(1,101)]
print(numbers) #普通输出，for之前可以添加计算过程
# 列表的切片：切片就是从主列表中获取子列表，切片即numbers[start:stop:step]，step为步长，注意是否包含，前数包含，后数不包含
numbers = list(range(10))
print(numbers[2:5])  #2开始5结束，不包含5
print(numbers[:6])  #0到6结束，不包括6
print(numbers[5:])  #5开始，到末尾结束
print(numbers[6:9:2])  #从6开始，到9结束，步长为2
print(numbers[:])  #包含所有元素
# 元组tuple：一种类似于列表的数据序列，元组不可变，不可以添加，删除，更新元素，一般用来保存重要数据，数据用小括号包括，元素之间用逗号隔开，字符串列表元组都支持索引，切片，遍历
student = (1001,'黎明',20) #一份元组数据
tup = 'a','b',10,'c'  #元组数据可以省略括号
tup = ()  #空元组
tup = (50,)  #单个元素元组
# 元组与列表用处与差别
# 元组用来存储不同信息，一个人的一个主体的不同信息，列表用来表示很多人的同类型数据
# 元组更多用来拆包，列表是循环遍历，元组不可变，不能改变，列表可以改，元组更安全
student = (1001,'黎明',20,176)
print('遍历多个数据：')
for i in student:
    print(i)

print('拆包得到多个变量：')
number,name,age,height = student
print('学号：',number)
print('姓名：',name)
print('年龄：',age)
print('身高：',height)
# 整体修改，不能更改单个元素
student = (1003,'daming',23,189)
print('修改完的数据：',student,type(student))

