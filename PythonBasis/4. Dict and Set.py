# 1. Dict structure
Dict = {key1 : value1, key2 :v alue2}
User = {'id':12,'name':'Tom','age':18}
Users = {'Tom': 'Male', 'Amy': 'Female'}


# 2. Get values in dict
user = {'id':123,'name':'Tom','age':18}
print(user['id'])
print(user['name'])
# If error with user[''], use get
print(user.get('name'))



# 3. Add elements in dict
user['height'] = 180
user['age'] = 19
print(user)



# 4. Iterate the elements in dict
# dict.items(): get the key-value pair and return list
# dict.key(): get all keys and return list
# dict.value(): get values and return list
for key,value in user.items():
    print(key,value)
print(user.items())
print(list(user.items()))

for key in user.keys():
    print(key)
    
for value in user.values():
    print(value)
    


# 5. Nested dict(dict in list)
students = [
    {'id':101,'name':'Tom','height':190},
    {'id':110,'name':'Amy','height':180},
    {'id':112,'name':'John','height':179},
]
for student in students:
    id,name,height = student['id'],student['name'],student['height']
    print(f 'The student number is {id}, her/his name is {name} and the height is {height}.')




# 6. Nested dict(list in dict)
students = {
    'Tom' : ['football','basketball'],
    'Amy' : ['badminton'],
    'Alice' : ['pingpong'],
}
for student,hobby in students.items():
    print(f'My name is {name}, and my hobby sports are {hobby}')



# 7. Nested dict(dict in dict)
students = {
    'Tom' : {'id':12,'height':180,'job':'teacher'}, 
    'Amy' : {'id':13,'height':179,'job':'nurse'},
    'Alice' : {'id':14,'height':168,'job':'writer'},
}
for name,stock in students.items(): # pack
    id,height,job = stock['id'],stock['height'],stock['job'] # unpack
    print(f'Student's name is {name}, and student number is {id}, height is {height}, job is {job}')



# 8. set()
s = set() # Empty set
s = set(1,2,33,33,4)  # Data Dedpulication
s = set([1,2,33,33,4])
Set methods:
len(set) # number of set elements
for i in set # elements iteration
set.add(key) # add new key
set.remove(key) # drop one key
set.clear() # clean the whole set
i in set # check if one element in set, same as i not in set

