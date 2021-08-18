import math
import time
x = [1,2,3,4,5,6,7,8,9,10]
print('choose a number between 1 and 10')
choice=int(input())


while choice not in x:
    print("I said between 1 and 10")
    choice=int(input())
print('timed 2')
choice2=int(input())
fonction1=choice*2
while choice2 != fonction1:
    print('Wrong!')
    choice2=int(input())
print("add 4")
fonction2=choice2+4
choice3=int(input())
while choice3 != fonction2:
    print('Wrong!')
    choice3=int(input())
print("You'v got"+ str(choice3)+ ' years to live \nBye:)')
time.sleep(4)
