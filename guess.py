import random 

r = random.randint (1,100)
while True:
    num = input('please guess a number: ')
    num = int(num)
    if num == r:
        print('Congrats! You are right! ')
        break
    elif num > r:
    	print('You are bigger than the answer! ')
    elif num < r:
    	print('You are smaller than the answer! ')

