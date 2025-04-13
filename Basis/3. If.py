# 1. If
grades = [60,70,99,89,34,56]
for grade in grades:
    print('Your grade is: ',grade)
    if grade >= 60:
        print('Congratulations! passed.')
    else:
        print('Sorry, not passed.')



# 2. Conditional Statement
# a == b (equal to)  a != b (not equal to)  a > b (greater than)  a >= b (greater than or equal to)   a < b (less than)  a <= b (less than or equal to)
# in : contain  not in : not contain
# Logic operators : and (Returns True only if all conditions are true);  or（Ruturns True only if at least one condition is true）  not (not)
# Using parentheses to group the conditions

grade = 70
print('passed',grade >= 60)

print('not passed',grade < 60)

print('full score',grade == 100)

print('not full score',grade != 100)

print('middle-level grade',grade >= 70 and grade < 90)

print('passed and the grade end with "0" ',grade >= 60 and (grade == 60 or grade == 70 or grade == 80 or grade == 90 or grade == 100))






# 3. If Condition
# Single if
grade = 70
if grade >= 60:
    print('passed')

# With else
if grade >= 60:
    print('passed')
else:
    print('not passed')
    
# With multiple elif and else with multiple conditions and only one condition can be operated
if grade <= 60:
    print('not passed')
elif grade < 80: 
    print('great')
elif grade <90:
    print('middle')
else:
    print('excellent')
    




# 4. Practice
results = []
numbers = [2,3,5,8,7,4,1,6]
aim_number = 8
for number1 in numbers:
    for number2 in numbers:
        if number1 + number2 == aim_number and (number1,number2) not in results:
            print('These two numbers puls result is 8 : ',number1,number2)
            results.append((number1,number2))
            results.append((number2,number1))

