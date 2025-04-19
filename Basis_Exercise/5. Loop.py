# 打印字母a-z
import string
for i in string.ascii_letters: # 本身是一个包含a-z的属性方法，直接进行生成
    print(i)
# 打印1-10
for i in range(1,11):
    print(i)
# 打印1-100和
a = 0
i = 1
for i in range(1,101):
    a += i
    i += 1
print(a)
# 打印1-100偶数和
print(sum(range(1,101)))
tatol = 0
for i in range(1,101):
    if i % 2 == 1:
        continue
    tatol += i
print(tatol)
print(sum(i for i in range(1,101) if i % 2 == 0))
# 输出元素与下标
a = [1,2,3]
# 函数：enumerate(a)函数产生数组的（下标index，数值item）数据对
# 用for index,item in enumerate(a)可以依次取出index和item
# 在字符串前面加上f，可以带格式的访问变量，是f-string语法
for index,item in enumerate(a):
    print(f'Item{item} has index{index}')

# 同时遍历多个数据
a = [1,2,3]
b = (4,5,6)
for i,j in zip(a,b):
    print(i+j,i/j)
print(list(zip(a,b))) # 占内存
# 不同序列可以通过zip函数打包在一起，序列为列表，元组等，zip组建的是数据对


