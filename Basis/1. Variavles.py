# 
message = 'hello python'
print(message)
message = 'nihao'
print(message)
# 命名规则：只包含数字字母下划线，不能用数字开头，其他两个可以开头，不能包含空格，用下划线分割，不得用函数命名
# 练习：类的模块的继承与不同模块的传递：变量三次更新：小明小李小张
# 2、字符串：前端用户输入，日志文件，网络爬虫，数据库，字符串例如‘我的名字是李华’，‘my name is lihua’，字符串单双引号都可以进行圈注。双引号与单引号都能进行声明，双引号中有单引号或者单引号中有双引号都可以，不能单引号双引号同类叠加使用
# 错误示例：‘我的名字是‘黎明’’
# 更改字符串大小写方法：.upper()  .lower()
sentence = 'My name is Liming'
sentence.upper()
print(sentence.upper())
sentence.lower()
print(sentence.lower()) #用了函数要一起输出
# 在字符串中使用变量的方法 f'{},{}' 拼装法，也即字符串的格式化
name = '黎明'
country = '香港'
print(f'我的名字是{name},我来自于{country},请多多关照吧')
# 或者命名输出
message = f'我的名字是{name},我来自于{country},请多多关照吧'
print(message)
# 字符串中使用空白符号：\t制表符（空格），\n换行符
print('hello\tworld')
print('hello\nworld')
# 删除字符串前后的空白，带有空格的数据不同
sentence = '   python    '
sentence = sentence.strip()
print(sentence) #变量函数一体化，一定要整体使用，可以另行赋值
# 练习：类的模块的继承与不同模块的传递
name = 'xiaoming'
gender = 'female'
message = f'我的名字是{name},我是一个{gender}孩'
print(message)
message = message.upper()
print(message)
# 3、整数与小数的运算：整数是int，包括正负，小数是float，即浮点数，也包括正负
# 计算规则：加减乘除，括号改变优先计算级
a,b = 3,4  #可以给多个变量赋值
c1 = a + b
c2 = a - b
c3 = a * b
c4 = a / b
print(c1,c2,c3,c4)  #可以输出多个结果
# 练习：类的模块的继承与不同模块的传递
a,b,c = '西红柿','黄瓜','大葱'
a,b,c = 10,2.99,4.7
d = a*3 + b*4 + c*2
print(d)
xhs_price,amount1 = 10,3
hg_price,amount2 = 2.99,4
dc_price,amount3 = 4.7,2
total_price = xhs_price * amount1 + hg_price * amount2 + dc_price * amount3
print(total_price)
# 4、变量的类型：字符串str，整数int，小数浮点数float，检测数据类型用函数type，即print(type(message))，对应的转换函数为int(),float(),str()
a = '45'
b = int(a)
print(type(b))
