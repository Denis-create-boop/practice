from random import *
from bd.questions_db import Categories, Words


CATEGORIES = Categories()
WORDS = Words()


def display_hangman(tries):
    stages = [
        '''

                  вы повесили человечка(((
                      ----------
                      |        |
                      |        O __-- ххх
                      |       \\|/
                      |        |
                      |       / \\
                      |
                      |_
        ''',
        '''
                      ----------
                      |        |
                      |        O __-- помогите
                      |       \\|/
                      |        |
                      |       /
                      |
                      |_
        ''',
        '''
                      ----------
                      |        |
                      |        O __-- прошу не надо
                      |       \\|/
                      |        |
                      |
                      |
                      |_
        ''',
        '''
                      ----------
                      |        |
                      |        O __-- ааааа
                      |       \\|
                      |        |
                      |
                      |
                      |_
        ''',
        '''

          уже есть голова и туловище, повнимательней
                      ----------
                      |        |
                      |        O __-- где я?
                      |        |
                      |        |
                      |
                      |
                      |_
        ''',
        '''
                      ----------
                      |        |
                      |        O
                      |
                      |
                      |
                      |
                      |_
        ''',
        '''

                   пустая виселица
                      ----------
                      |        |
                      |
                      |
                      |
                      |
                      |
                      |_
        '''
    ]
    return stages[tries]


def main():

    category = choice(CATEGORIES.show_categories())
    writed_letters = []  # список уже названных букв


    print(f'''     
                                Давайте поиграем в угадайку слов
                                Слово из категории {category}
                                ''')
    # загаданное слово
    word = choice(WORDS.show_words(category))
    
    letters = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    tries = 6  # количество попыток
    print(display_hangman(tries))
    print(letters)
    print(f'''
                                    введите букву или слово целиком
                                    если желаете подсказку напишите номер буквы которую хотите открыть
                                    ''')
    letter = input()

    count = 0
    while True:
        total = 0
        # если ввели номер буквы тоесть просят подсказку
        if letter.isdigit():
            if count < 3:
                index = int(int(word) - 1)
                letters = letters[:index] + letter[index] + letters[index + 1:]
                print(letters)
                total += 1
                count += 1
                print('осталось', 3 - count, 'подсказки')
            else:
                print('извините у вас больше нет подсказок')

        # проверяем что такая буква не названа
        elif letter in writed_letters:
            print('                  Вы уже называли букву', letter)

        elif letter == word:
            print(f'''
                                     Поздравляем вы угадали слово
                                     Желаете сыграть ещё? да/нет
                                     ''')
            answer = input()
            if answer == 'нет':
                break
            else:
                play(word)

        writed_letters.append(letter)
        
        if letter in word:
            letter_index = word.index(letter)
            letters = letters[:letter_index] + word[letter_index] + letters[letter_index + 1:]
            word = word[:letter_index] + ' ' + word[letter_index + 1:]
            total += 1

        if total > 0:
            print(f'''
                                    Поздравляем вы угадали букву

                                    {display_hangman(tries)}

                                    Введите букву или слово целиком из категории {category}
                                    если желаете подсказку напишите номер буквы которую хотите открыть

                      ''')
            if letters == letter:
                print(f'''
                                    Поздравляем вы угадали слово
                                    Желаете сыграть ещё? да/нет
                          ''')
                answer = input()
                if answer == 'нет':
                    break
                else:
                    play(word)
            else:
                print(letters)
                letter = input()

        elif total == 0:
            tries -= 1
            if tries == 0:
                print(f'''
                                   Вы проиграли, загаданное слово {letter},
                                   {display_hangman(tries)}
                                   Желаете сыграть ещё? да/нет
                          ''')
                answer = input()
                if answer == 'нет':
                    break
                else:
                    play(letter)

            else:
                writed_letters.append(letter)
                print(f'''
                                   Вы не угадали, осталось попыток {tries} {display_hangman(tries)}
                                   введите букву или слово целиком из категории {category}
                                   если желаете подсказку напишите номер буквы которую хотите открыть
                      ''')
                print(letters)
                letter = input()


def play():
    pass

if __name__ == "__main__":
    main()
