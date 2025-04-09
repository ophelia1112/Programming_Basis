# 1. Variables
message = 'hello python'
print(message)


# 2. Rules about defination：only contain numbers, words, and underline; numbers can not used in head position


# 3. How to change words in upper or lower : .upper()  .lower()
sentence = 'My name is Tom'
sentence.upper()
print(sentence.upper())

sentence.lower()
print(sentence.lower())


# 4. Use variables in str : f'{variable1},{variable2}' 
name = 'Tom'
country = 'USA'
print(f'My name is {name}, I come from {country}.')


# 5. Tab: \t
Newline: \n
print('hello\tworld')
print('hello\nworld')


# 6. Remove the space
sentence = '   python    '
sentence = sentence.strip()
print(sentence)



# 7. Calculation
a,b = 3,4  
c1 = a + b
c2 = a - b
c3 = a * b
c4 = a / b
print(c1,c2,c3,c4) 
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
