from random import choice

list = ['бесспорно', 'предрешено', 'никаких сомнений', 'определенно', 'можешь быть уверен в этом', 'мне кажеться да', 
		'вероятнее всего', 'хорошие перспективы', 'знаки говорят - да', 'да', 'пока не ясно, попробуй снова', 'спроси позже',
		'лучше не рассказывать', 'сейчас нельзя предсказать', 'сконцентрируйся и спроси опять', 'даже не думай', 'мой ответ - нет', 
		'по моим данным - нет', 'перспективы не очень хорошие', 'весьма сомнительно']

print('добро пожаловать')
print()
print()

b = choice(list)
while True:
    print('задай мне вопрос')
    a = input()
    print(b)
    print()
    print('хотите задать еще один вопрос?')
    a1 = input()
    if a1 == 'да':
        b = choice(list)
    else:
        print('возвращайся если возникнут вопросы')
        break

  
