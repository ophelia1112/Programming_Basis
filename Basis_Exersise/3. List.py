# range函数生成列表
data = (list(range(1,21)))
print(data)
lost = range(1,21)
print(list(lost))
# range和推导式，推导式就是方便的列表生成
numbers = [i for i in range(1,201) if i % 10 == 0]
print(numbers)
# range生成字符串
numbers = [str(i) for i in range(1,21)] # 用str转化你要遍历的首变量
print(numbers)
# 移除列表重复元素
# 使用list,set函数去除，问题是会顺序不一样
a = ['1',1,'1',2]
b =list(set(a)) #借助set函数去重
print(b)
# 或者遍历循环，问题是浪费时间
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)
# 列表的排序
lista = [20,40,30,50,10]
lista.sort(reverse = True) # 直接作用不用赋值
print('排序的结果为:',lista)
