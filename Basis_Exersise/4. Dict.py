# 创建字典的方法
d = {'a':1,'b':2}
print(d['a']) # 访问字典数据
print(d['b'])
print(d['a'] + d['b']) # 实现加和
d = dict(a = 1,b = 2) # 创建字典的第二种方法
print(d)
# 给字典添加值，字典数据无序，不重复
d['c'] = 3
print(d)
# 对字典用函数：d.values()可以返回一个字典所有的values  sum()函数对一个序列直接求和
print(sum(d.values()))
# 字典的过滤
d = {'a':1,'b':2,'c':3}
d = {key:value for key,value in d.items() if value <= 1}
# 字典的推导式：{key:value for 循环 if 条件}  同时 d.items()能够同时返回每个键值对
print(d)
d = {key:value*8 for key,value in d.items() if value <= 1} # 还可以对value进行操作
print(d)

# 字典的格式化输出
from pprint import pprint  # pprint会产生比较整齐的输出
d = {'a' : list(range(1,11)),  # list(range())可以把一串数字或者字符串变成列表
     'b' : list(range(11,21)),
     'c' : list(range(21,31))}
pprint(d)
print(d) # 普通打印就是没有格式

# 字典的多层索引访问
d = {'a' : list(range(1,11)),
     'b' : list(range(11,21)),
     'c' : list(range(21,31))}
print(d['b'][2]) # 访问字典里面的列表中的元素，用下标法
print(d['b'][2]) # ctrl+d 复制一行代码

# 遍历字典
d = {'a' : list(range(1,11)),
     'b' : list(range(11,21)),
     'c' : list(range(21,31))}
for key,value in d.items():
    print(f'{key}的值是{value}')
    # print(key,'has value',value)