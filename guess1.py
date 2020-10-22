import random 

r = random.randint (1,100)
count = 0 
while True:
    count = count + 1
    num = input('please guess a number: ')
    num = int(num)
    if num == r:
        print('Congrats! You are right!')
        print('This is your', count , 'th guess')
        break
    elif num > r:
        print('You are smaller than the answer!')
    elif num < r:
        print('You are bigger than the answer!')
    print('This is your', count , 'th guess')