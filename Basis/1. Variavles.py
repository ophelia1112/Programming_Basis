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
