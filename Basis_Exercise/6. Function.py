# 编写加速度函数  acceleration
# 创建函数，计算加速度，初始速度v1，结束速度v2，初始时间t1，结束时间t2
def a(v1,v2,t1,t2):
    return (v2-v1)/(t2-t1)
print(a(0,10,0,20)) # 重复用，同时能在其他文件中调用

# 方法不存在怎么解决
# import math
# print(math.cosine(1))
# 查询math怎么计算cosine值，百度搜索，或者查看dir(math)得到模块所有方法，找到正确方法名，或者求助即print(help(math.cosine))
import math # 引入数学模块
print(dir(math)) # 查看数学模块所有的方法名
print(help(math.cos)) # 查看方法注释
print(math.cos(1))

# 函数参数数目错误
import math
print(math.pow(2,3)) # 需要两个参数，只有一个会报错 即前面的数的后面的平方
# 当不会使用函数的时候就用 print(help(math.pow)) 可以看一个模块下的某个函数的使用方法

# 函数的调用
def foo(a=1,b=2):
    return a+b
x = foo() - 1 # 此处不能直接用foo-1因为foo是个对象，不能与整数进行加减，调用函数才能进行计算
print(x)

# 参数默认赋值放在后面
def foo(b,a=2):
    return a+b
print(foo(2,1))
print(foo(2))

# 函数的全局变量
c=1
def foo(): # 函数在定义的时候是无法执行代码的
    return c
c=3 # 全局变量更新
print(foo())

# 函数的局部变量
c=1
def foo():
    c=2 # 函数内可以访问函数外的全局变量，但是局部变量是更为优先的
    return c
c=3
print(foo())

# 怎么把局部变量声明为全局变量
def foo():
    global c # 局部变量变为全局变量
    c=1
    return c
foo()
print(c)
