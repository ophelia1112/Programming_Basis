# 给文件内容乘数字
with open('被乘文件.txt') as fin,open('乘完的文件.txt','w') as fout: # with与逗号能打开多个文件
    for line in fin: # 按行读取
        if 'x,y' in line: # x,y是标题行
            fout.write(line)
        else:
            x,y=line.strip().split(',') # 分成两行
            x=int(x)*2 # 行是字符串转换为整数并进行乘积
            y=int(y)*2
            fout.write(f'{x},{y}\n') # 按照格式书写
# debug一步一步看

# 计算最值与平均值，成绩文件，利用函数
def compute_score():
# 把文件中的值读取出来
    scores=[]

    with open('成绩.txt') as f:
        for line in f:
            line=line.strip()
            fields=line.split(',')
            scores.append(int(fields[-1]))
        print(scores)

    max_score=max(scores)
    min_score=min(scores)
    average_score=round(sum(scores)/len(scores),2)
    return max_score,min_score,average_score
max_score,min_score,average_score=compute_score()
print(max_score,min_score,average_score)



# 文件合并，将两个文件合在一起并放在另一个新的文件中
with open('合并两个文件后的文件.txt','w',encoding='utf8') as f:
    for fname in ['合并文件1.txt','合并文件2.txt']:
        with open(fname,encoding='utf8') as fin:
            for line in fin:
                f.write(line)


# 文件内容里面有交集
def get_intersact(fname):
    number=[]
    with open(fname,encoding='utf8') as f:
        for line in f:
            number.append(line.split(',')[1]) # 第二列中有交集，逗号分隔
        return number
number1=get_intersact('合并文件1.txt')
number2=get_intersact('合并文件2.txt')
for i in set(number1).intersection(set(number2)):
    print(i)



# 计算爱好的喜欢人数
# 为字典
like_count={}
with open('爱好.txt',encoding='utf8') as fin:
    for line in fin:
        line=line[:-1] # 内容为多行加换行符，取-1便能取全
        # 解析数据
        # 姓名和爱好空格分隔
        names,likes=line.split(' ')
        # 爱好之间逗号分隔
        like_list=likes.split(',')

        for like in like_list:
            if like not in like_count:
                # 初始化
                like_count[like]=0
            # 有值再加
            like_count[like]+=1
# 遍历键，值并以元组的形式存储
for key,value in like_count.items():
    print(key,value)

# 实现文件的关联
# 拼接直接放后面，关联则为按照某种格式或者列进行关联
grade_dict={} # 成绩拼到学生信息，实质上只有名字需要拼接
with open('关联文件1.txt',encoding='utf8') as f1:
    for line in f1:
        number,grade=line.strip().split(',')
        grade_dict[number]=grade

f3=open('关联完的文件.txt','w',encoding='utf8') # 待写入的文件
with open('关联文件2.txt',encoding='utf8') as f2:
    for line in f2:
        number,name=line.strip().split(',')
        grade=grade_dict[number]
        f3.write(f'{number},{name},{grade}\n')
f3.close()
# 原理就是利用字典不断存储信息













