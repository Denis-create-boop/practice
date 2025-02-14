from random import *
from math import *
print('Добро пожаловать в числовую угадайку')
print('введите максимальное число')
b = int(input())
def is_valid(num):

    if 1 <= num <= b:
        return True
    return False


total = 1
a = randint(1, b)

while True:
    print('введите число от 1 до', b)
    
    x = int(input())
    if is_valid(x):
        ceil(x)
        if x < a:
            total += 1
            print('ваше число меньше загаданного числа, попробуйте еще раз')
        elif x > a:
            total += 1
            print('ваше число больше загаданного числа, попробуйте еще раз')
        else:
            print('вы угадали поздровляем')
            print('спасибо что играли в числовую угадайку, еще увидимся')
            a = randint(1, b)
            print('количество попыток =', total)
            print('хотите сыграть еще? да или нет')
            gwe = input()
            if gwe == 'да':
                print('введите максимальное число')
                b = int(input())
            else:
                break
    else:
        print('а может введем целое число?')
        x = int(input())
