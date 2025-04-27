# 1. List
animals = ['cat','dog','chicken']
print(animals)
print(type(animals))


# 2. Get elements in list
# Indexing method
print(animals[0])
print(animals[-1])



# 3. Add, delete, revise elements in list
# revise
animals[0] = 'snake'
print(animals)

# add
animals.append('whale')
print(animals) 

# remove
animals.remove('snake')
print(animals)


# 4. Get the length of list and sort elements in list
grades = [11,89,45,67,87,34]
grades.sort()
print(grades)


# 5. Sort elements in list and set reverse direction
grades.sort(reverse=True)
print(grades)


# 6. Use sorted to keep original list unchanged
grades2 = sorted(grades,reverse=True)
print(grades,grades2)


# 7. Use len() to calculate the length of the list


# 8. Loop
list = ['Tom','Lily','Amy']
for name in list:  
    print(name) 



# 9. Use range(start,end,step) to generate random numbers list
for number in range(1,21):
    print(number)


# 10. List calculation
data = [1,2,3,4,5,6,7,8]
print('Max value: ',max(data))
print('Min value: ',min(data))
print('Values sum: ',sum(data))
print('Lens of values: ',len(data))


# 11. List comprehension
# generate square list of the numbers from 1 to 100
numbers = [i*i for i in range(1,101)]
print(numbers)

# generate square list of the even numbers from 1 to 100
numbers = [i*i for i in range(1,101) if i % 2 == 0] 
print(numbers)

# generate square list of the odd numbers from 1 to 100
numbers = [i*i for i in range(1,101) if i % 2 ==1]
print(numbers)



# 12. List slicing----numbers[start:stop:step]
numbers = list(range(10))
print(numbers[2:5]) 
print(numbers[:6]) 
print(numbers[5:])
print(numbers[6:9:2]) 
print(numbers[:]) 



# 13. Tuple(Can not be changed)
student_tuple = (1001,'Tom',20) 
tuple1 = 'a','b',10,'c'  "can not use parentheses"
tuple2 = ()
tuple3 = (50,) 

# Use tuple to pack and unpack data
student = (1001,'Tom',20,176)
for i in student:
    print(i)

print('Unpack student data: ')
number,name,age,height = student
print('StudentID: ',number)
print('Name: ',name)
print('Age: ',age)
print('Height: ',height)

# revise 
student = (1001,'Tom',23,189)
print('Revised data: ',student,type(student))
