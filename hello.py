name = 'hisheng'
print ('my name is ' + name)
print (2 + 2)

def hello():
    print('haha')
    print('hi baby')

hello()

def say(name):
    print ('say bye ' + name )

say(name)

def sum(x,y):
    return x + y

print(sum(10,20))

import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

