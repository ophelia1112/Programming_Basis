# 1. input()
number = input('please input one number:')
number = int(number)  # input function just see content as str so need to do data transformation
print(f'The number you have input is {number},its square is {number * number}')


# 2. while and input
# exercise
number,sum_value = 1,0
while number <= 100:
    sum_value += number
    number += 1
print(sum_value)

# 3. while, input and break
while True:
    weight = input('Please input the weight of your goods（kg）, and input "quit" to quit:')
    if weight == 'quit':
        break
    else:
        weight = float(weight)
        if weight <= 0:
            print('wrong weight')
            continue
        if weight < 1:
            print('express fee of your goods is $7')
        elif 1 < weight < 3:
            price = 7 + 2 * weight
            print(f'express fee of your goods is {price}')
        elif weight >= 3:
            price = 7 + 3 * weight
            print(f'express fee of your goods is {price}')
        else:
            print('wrong content your input',weight)

# 4.game
import random
target = random.randint(1,100)
success = False  
time = 0
while time <= 10:
    number = input('please input the number you guess:')
    if not str(number).isnumeric(): 
        print('the content you input is not a number, please input again!')
        continue
    number = int(number) 
    if number == target:
        print('Congratulations, you're right!')
        success = True
        break
    elif number < target:
        print(f'the number you input is {number}, too small!')
    else:
        print(f'the number you input is {number}, tpp large!')
    time += 1
else:
    print(f'you have already guessed for ten times, the right answer is {target}!')
