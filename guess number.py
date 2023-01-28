from random import randint
computer = randint(0,10)
introdution = '''-----------------------------------------------------
            Guess number i'm thinking
-----------------------------------------------------'''
print(introdution)
num = float(input('What number am thinking of 0 to 10?'))
if num == computer:
    print('Congratulations! You got it rigth')
else:
    print('You got it wrong. The number i thought is {}'.format(computer))
