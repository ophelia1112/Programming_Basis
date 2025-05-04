
# 第一种是存储到纯文本文件中，例如txt文件，另一种是存储到excel文件中，或者将数据存储到数据库例如MySQL中
# 数据存储使用方法：首先将来自于爬虫或者用户输入的数据直接存储在文件中并进行保存，每次使用时从文件中读取已经保存的数据，并基于这些数据做处理，每次打开与运行程序，都能读取之前的数据，实现固化存储
# 文件读取操作：读取整个文件的内容
f = open('访客名单.txt',encoding = 'utf8') #f是文件的对象，变量名字是随意的，其中的open函数可以打开一个文件，在函数里面给出文件的名字，文件中有中文就要加上编码参数，编码参数是utf8，国家通用编码是utf8,也有一个文件编码格式是gbk只用作汉语
content = f.read() #文件名.read()函数可以读取整个文件的内容
print(content)
f.close() #最后是需要关闭文件的，不然可能会数据丢失报错，但是前方代码执行报错，close函数执行不到，可能会数据丢失报错，这种情况下怎么解决：
# 解决方法：用with语法读取文件
with open('访客名单.txt',encoding = 'utf8') as fin: #with是python中的关键字，是表示接管“资源自动关闭”等事宜的语句，open函数打开文件，文件中有中文加上国际通用编码，后面的as fin是给了一个文件对象名字
    content = fin.read()
    print(content) #由此最后不需要close函数进行处理，with语句会自己进行文件的关闭以及其他处理工作

# 怎样按行读取数据：用 for line in fin 进行按行读取数据
with open('访客名单.txt',encoding = 'utf8') as fin:
    for line in fin:
        # 这里默认会有一个结尾的换行符，有两种去除换行符的方法。以下示例
        # line = line[:-1] #去掉末尾的换行符，-1即最后一个字符，末尾字符符号有含义，多用此，一般多用这种方式，他是去除最后一个位置数据
        line = line.rstrip() #去掉反方向的空白，即去掉末尾的换行符，如果说末尾数据符号无含义，多用此方法，他是去除空白
        print(line)

# 怎么把行读取到列表：fin.readlines() 可以读取数据到列表
with open('访客名单.txt',encoding = 'utf8') as fin:
    lines = fin.readlines()
    lines = [x[:-1] for x in lines]
    print(lines,type(lines))
    # 打印结果中能够看到换行符\n，换行符是一个整体的字符，可见的换行符是要进行处理的，本身应该不可见，就用切片或者rstrip()进行处理
# 批量去掉后面的换行符，即用x变量。指定到-1的位置，将x变量也就是所指的列表中的对象进行逐一遍历，进行去除

# 文件读取的练习题：文件读取实现英汉翻译，构建了英汉翻译字典，符号与缩进要严谨，数据是自身扩展的，相当于实现了翻译功能
eng_dict = {}
with open('英汉词典.txt',encoding = 'utf8') as f:
    for line in f:
        line = line.rstrip()
        fiedls = line.split(',') #split会得到多个字段，但是不确定是哪个，有的时候得到的字段是无用的不需要的脏数据，故进行判断，数据是用逗号隔开的，括号内是逗号
        if len(fiedls) != 2: #筛选符合条件的数据
            continue #把错的数据掠过，因为拆分的是字典数据，没有拆成两个数据那就不是字典，掠过，常见的去除脏数据的方法
        english,chinese = fiedls #可能会报错，因为数据中可能有空白数据或者脏数据，会报错，因此要做判断，即上方判断
# 元组数据可以拆包，列表也可以
        eng_dict[english] = chinese #构建字典
        print(eng_dict)
while True:
    stock = input('请输入您要查询的英文单词，输入quit推出查询：')

    if stock == 'quit':
        break
    if stock in eng_dict:
        print('查询结果是：',eng_dict[stock])  #字典[我们所输入的key]，访问对应的value
    if stock not in eng_dict:
        print('数据不存在')

# 怎样将数据写出文件：把一个大字符串写到文件里面，并且按照行写出文件
# 数据写在文件里面，实现数据的保存
with open('数字列表.txt', 'w', encoding = 'utf8') as fout: # 新建数字列表文档，w是写文件的意思，编码是utf8
# 拓展：t是文本模式，默认的  x是写模式，新建一个文件，文件存在会报错   b是二进制模式   +打开一个文件进行更新，可读可写   r只读
# rb二进制的方式打开文件并且只读，一般是非文本文件，如图片   r+读写   rb+二进制打开并且读写，图片文件   w写入，文件存在从头开始编辑，文件不存在创建文件，文件已经存在清空文件重新写入
# w+打开文件用于读写   a打开文件用于追加，光标在末尾，文件不存在，创建新文件加入   ab二进制打开文件并追加，光标末尾，不存在创立新文件
# a+打开文件读写   ab+二进制打开文件用于追加
# 以下代码已经
    number = 998
    fout.write(str(number))
# fout调用write可以写入内容，只能写入字符串，不能写入数字，需要将数据转换成字符串

# 如何按行写出文件
with open('写出数字列表.txt','w',encoding = 'utf-8') as fout: #w即write，写出文件 同理中文encoding，只能写出字符串，不能数字
    for number in range(134): #100个数字写到一个文件，数字需要转换成字符串
        fout.write(str(number) + '\n') # 想要换行，自己加上换行

# 改进婚礼礼金程序练习
# 用w的写入模式，打开文件“婚礼礼金.txt”，并用while true循环，输入存储姓名与礼金，数据存储到文件里，每行一个数据，quit退出，退出循环后，重新按行读取，礼金读取到list列表中，并加和，最高最低值，平均值计算
# 见8.1


# 相对路径与绝对路径
# 文件的路径指定：文件在电脑别的存储位置，即用路径访问，目录1/目录2/文件.txt，若访问电脑上任意一个文件，有绝对路径和相对路径之分
# 绝对路径：从D:等盘符开始写路径，相对路径是从当前目录寻找文件或者子目录，可以复制路径引用
# 由于\n,\t有特殊含义，反斜线分割路线前面加r，或者直接/正斜线
# file_path = r'D:\workbench\zero\current file\fangke.txt' 也可以\\
# file_path = 'D:/workbench/zero/current file/fangkr.txt'


# 判断文件或者目录是否存在
# import os
# file_path = 'D:/workbench/zero/current file/fangke.txt'
# print(os.path.exists(file_path))
# 由此来判断文件是否存在，返回true false

# JSON数据格式与文件
# 诉求：将列表与字典中的数据结构直接存到txt中，实现格式化的读取与保存，json是实现诉求的库，引入库import json，json.dumps(data)，data可以是字符串，列表和字典，可以把对象转换成为字符串并写到文件里，而json.loads(str)可以把大字符串读取成对象成为list或者dict
# 将对象转换成大字符串
import json
data = [1,2,3,4,5]
print(json.dumps(data),type(json.dumps(data)))
data = {
    number:number*number
    for number in data
    if number % 1 == 0
}
print(json.dumps(data),type(json.dumps(data)))

# 将字符串反转为对象，变成python的对象
import json
info='''
{"1": 1, "2": 4, "3": 9, "4": 16, "5": 25}
'''
print(json.loads(info),type(json.loads(info)))

# 使用JSON完成学生数据保存
# 逻辑：加载文件的词典文件为“成绩录入json,txt”，文件存在的话，加载到字典grade_dict，文件不存在新建成绩字典grade_dict={}，利用while true输入成绩，每行成绩形如“小明 90”，使用str.split拆分成绩与姓名，存入字典name是键，grade为值，quit退出循环，再用grade_dict更新保存到json文件中
import os # 判断文件是否存在
import json # 对字符串文件进行转化，此处转换为字典
file_name = '成绩录入json.txt' # 创建的文件名称，文本文件名称
grade_dict = {} # 首先建立空字典
if os.path.exists(file_name): # 如果成绩录入的文本文件存在的话
    with open(file_name,encoding='utf-8') as f: # 打开原有文本文件
        grade_dict = json.loads(f.read()) # 空字典就是读取之后文件的内容放到字典里面，并以字典形式出现在文件中

print("### 读取以后的内容") # 由于utf-8有时候会对文本进行转换读取，会在文档中出现乱码，故可以在此处增加代码看输出内容
for key,value in grade_dict.items():
    print(key,value)

while True: # 输入数据循环的过程
    print('#'*20) # 分隔符
    info=input('请输入姓名与成绩：')
    if info == 'quit':
        break
    fields = info.split()
    if len(fields) != 2:
        continue
    name,grade = fields
    grade = int(grade)
    # 前面创建的空字典，键与值的形式与顺序进行赋予
    grade_dict[name] = grade

# 退出循环进行文件的存储
with open(file_name,'w',encoding='utf-8') as f:#文件清空，存储最新数据
    f.write(json.dumps(grade_dict))



# 异常处理机制
# 传统方式是输入一个错误的数据，整个程序都将退出，但是在报错之前，对输入数据进行判断进行反馈，更改不合适的数据，而异常是python自身的对象，程序不对便会反馈，脚本发生异常应该捕获处理
# 一般异常有Exception即常规错误的基类（大类，包括所有错误），ZeroDivisionError除（或者取模）零（无法除0），IOError输入输出操作失败，ImportError导入对象模块失败，KeyError映射中没有这个键，SyntaxError Python语法错误，ValueError无效参数
# 在运行中发生错误时候对其进行修改捕捉
# 捕捉异常用try: 与except，即捕获异常，实现异常处理机制，不直接退出
grades=[]
while True:
    grade=input('请输入成绩：')
    try: # 下方可以用多行代码，下方有except接着运行
        grade=int(grade)
    except ValueError as e: # e可以改
        print('输入的数据有误，检查以后重新输入，信息为：',e)
        continue
    grades.append(grade)
    print(grades)

# 不同形式写法
# 1、捕获具体的异常，即try:  except ValueError as e:
# 2、捕获所有异常的父类Exception: try: except Exception as e:
# 3、不写异常对象，捕获所有异常种类。但是得不到具体的异常对象变量e，无法打印日志


# 另一种组合try:  except: finally，finally是不论是否有异常都执行，一般用于关闭资源，except与finally选择至少一个，with比finally好用
# 三种皆用
fin = open('写出文件','w')
try:
    while True:
        data = input('请输入数字：')
        data = int(data)
        fin.write(str(data) + '\n')
except Exception as e:
    print('程序出现问题，信息为：',e)
finally:
    fin.close()
# 同理不同出错误地方都可以进行try与except
# 练习
file_name='学生成绩异常处理.txt'
with open(file_name,'w',encoding='utf8') as f:

    while True:
        try: # 越往上放处理的问题就越多
            info=input('请输入姓名与成绩：')
            if info=='quit':
                break
            fields=info.split()
            name,grade=fields
            name=str(name)
            grade=int(grade)
            f.write(f'{name},{grade}\n')

        except Exception as e: #一定要至少打印点日志
            print('程序出现问题：',e)
            print('你输入的信息是：',info,'可以继续输入')
















