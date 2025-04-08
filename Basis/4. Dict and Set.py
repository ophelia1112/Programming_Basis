# 字典dict：定义，字典是键值对的数据结构，根据键即key，设置与获取对应值value，语法是 dict = {key1:value1,key2:value2}
# 空字典 data = {}  个人信息字典  user = {'id':12,'name':'kiki','age':18}  创建多人信息 users = {'小明'：'男'，'小红':'女'}
# 访问字典中的值：通过键访问对应的值，即dict[key]可以获取对应的value，如果key不存在返回none
user = {'id':123,'name':'小明','age':18}
print(user['id'])
print(user['name'])
# 写user[grade]会报错，但是写get不会报错并且可以指定默认值
print(user.get('grade'))
print(user.get('grade',90))
# 字典添加键值对：使用dict[key] = value可以添加键值对，如果键不存在即新增这个值，如果键存在则覆盖值
user['height'] = 180
user['family'] = 6
print(user)
# 循环遍历字典数据方法：
# dict.items()：以列表的形式返回可遍历的（键，值）元组数组，常用于for遍历
# dict.key()：以列表的形式返回字典所有的键
# dict.value()：以列表的形式返回字典所有的值
for key,value in user.items():
    print(key,value)
print(user.items())
print(list(user.items()))
for key in user.keys(): #可以换成任何名字
    print(key)
for value in user.values():
    print(value)
grades = {'小明':89,'小花':90,'小东':23}
for name in grades.keys():
    print(name,grades[name])
print(grades.keys())
print(list(grades.keys()))
for grade in grades.values():
    print(grade)
print(grades.values())  #输出对象
print(list(grades.values()))
# 练习题
fruits = {'小明':'apple','小花':'orange','小张':'banana','小白':'pear'}
for name,fruit in fruits.items():
    print(f'朋友{name}最喜欢的水果是 {fruit}')

# 字典的嵌套：列表的元素是字典，即数据的嵌套，将字典存储在列表里，或者字典的值即value是列表，或者字典的value值是字典
# 例子：学生信息字典的列表，列表里面放字典
students = [
    {'id':101,'name':'xiaoli','height':190},
    {'id':110,'name':'xiaohua','height':180},
    {'id':112,'name':'xiaoling','height':179},
]
for student in students:
    id,name,height = student['id'],student['name'],student['height']
    print(f'学号为{id}的学生叫{name}身高是{height}')
# 字典的value是列表：喜欢的球类，嵌套的结构里面注意字典是冒号连接，并且列表字典之间用逗号，字典里面放列表
students = {
    'xiaohua' : ['足球','篮球'],
    'xiaoming' : ['羽毛球'],
    'xiaodong' : ['乒乓球'],
}
for student,habby in students.items(): #列表整体循环
    print(f'学生名字是{name},爱好是{habby}')
# 字典嵌套中字典的value值是字典，字典里面套字典
students = {
    'xiaohua' : {'id':12,'height':180,'job':'teacher'},  #字典里面套字典名字与字典是分离的，所以名字是一块，字典内容是一块
    'xiaoli' : {'id':13,'height':179,'job':'nurse'},
    'xiaozhang' : {'id':14,'height':168,'job':'writer'},
}
for name,stock in students.items(): #合包
    id,height,job = stock['id'],stock['height'],stock['job'] #拆包
    print(f'学生的名字是{name}学号是{id}身高是{height}工作是{job}')
# 练习：类的模块的继承与不同模块的传递
students = {
    'xiaozhang' : {'id':101,'grade':88},
    'xiaowang' : {'id':102,'grade':99},
    'xiaoli' : {'id':103,'grade':77},
    'xiaozhao' : {'id':104,'grade':85},  #字典里面套字典如何更改信息，也就是覆盖信息
}
students['xiaoli']['grade'] = 87 #字典里面套字典先调取外层字典，再调取内部字典，最后赋值，两次调取都是并列行事
print(students)
grades = []
for name,stock in students.items():
    id,grade = stock['id'],stock['grade']
    grades.append(grade)
grades.sort(reverse = True)
print(grades)
# 集合set：集合是一组无序并且没有重复元素的键集合，即key的集合，键没有前后顺序，所以集合不支持数字索引与切片，具体使用在于判断某个元素是否在集合中，消除输入数据的重复元素
# s = set() #空集合
# s = set(1,2,33,33,4)  #遍历实现数据的去重
# s = set([1,2,33,33,4])
# 集合支持的方法：
# len(set) 集合的元素个数
# for i in set 集合的遍历
# set.add(key) 新增一个key，重复的话自动去重
# set.remove(key) 删除一个key
# set.clear() 清空set
# i in set 判断元素是否在set集合中，同理 i not in set

# 练习题：比较难
students = {
    'xiaozhang' : ['足球','篮球'],
    'xiaowang' : ['篮球','乒乓球'],
    'xiaoli' : ['篮球','棒球','台球'],
    'xiaozhao' : ['乒乓球','羽毛球'],
}
likes = set()
for habbies in students.values():
    for habby in habbies:
        likes.add(habby)
print(likes)

# 列表和字典和集合的推导式：列表字典集合都有推导式
numbers = range(56)
# 一个列表，里面每个偶数数字的平房
data_list = [i * i for i in numbers if i % 2 == 0]
print('data_list', data_list)
# 一个字典，里面的key是偶数，value是他的平方，字典key是无序的
data_dict = { i : i * i for i in numbers if i % 2 == 0}
print('data_dict',data_dict)
# 一个集合，每个元素是偶数的平方，集合无序
data_set = {i * i for i in numbers if i % 2 == 0} #都是大括号，只不过只有键
print('data_set',data_set)