import random

secretNumber = random.randint(1,20)
print('猜测的数组在 1 到 20 间,你有6次机会')

for i in range(1,7):
    print('输入数')
    guess = int(input())

    if guess < secretNumber :
        print ('太小')
    elif guess > secretNumber :
        print ('太大')
    else:
        break

if guess == secretNumber :
    print ('太棒了 你对了')
else:
    print ('猜错了，正确答案是 ' + str(guess))