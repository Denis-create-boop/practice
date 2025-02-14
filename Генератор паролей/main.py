from random import *
print('введите длинну желаемого пароля')
x = int(input())
print('включать ли цыфры в пароль?')
ans = input()
print('включать ли заглавные буквы?')
up = input()
print('включать ли строчные буквы?')
a = input()
print('включать ли символы?')
sym = input()
chars = ''

def length(num):
    if len(chars1) == num:
        return True
    else:
        return False

def upp(num):
    chars = ''
    for i in range(num):
        chars += choice('QWERTYUIOPLKJHGFDSAZXCVBNM')
    return chars

def low(num):
    chars = ''
    for i in range(num):
        chars += choice('qwertyuioplkjhgfdsazxcvbnm')
    return chars

def dig(num):
    chars = ''
    for i in range(num):
        chars += choice('1234567890')
    return chars

def punct(num):
    chars = ''
    for i in range(num):
        chars += choice('!/?._-')
    return chars

if ans == 'да':
    chars += dig(x)

if up == 'да':
    chars += upp(x)

if sym == 'да':
    chars += punct(x)

if a == 'да':
    chars += low(x)

chars1 = sample(chars, x)
length(x)
print('введите количество паролей')
x1 = int(input())
for i in range(x1):
    chars2 = sample(chars, x)
    print(*chars2, end='')
    print()
