from random import *
from database.questions_db import Categories, Words
from display import display_hangman



CATEGORIES = Categories()
WORDS = Words()
LIST_COMMAND = [1, 2]
ADMIN_LOGIN = "admin"
ADMIN_PASSWORD = "password"



def main():
    """Основная функция программы"""
    # вопрос о том что хочет совершить пользователь
    question = """
                                            Здравствуйте, выберите действие:
        1 - Работа с БД
        2 - Играть в угадайку слов"""

    print(question)
    print()
    answer = check_number(flag=True)
    commands_dict = {
        1: "",
        2: play,
    }

    commands_dict[answer]()




def check_number(len_word=None, number=None, flag=False):
    """функция для проверки правильности ввода цифр"""
    global LIST_COMMAND
    # проверяем если передаеться флаг то это начальная страница где выбираеться действие программы
    if flag:
        answer = input("==>> ")
        try:
            answer = int(answer)
            if answer in LIST_COMMAND:
                return int(answer)
            else:
                print("Введене неверная команда")
                check_number(flag=True)
        except:
            print("Пожалуйста введите число, номер действия")
            check_number(flag=True)
    # если флаг не передаеться то проверяем что число не превышает длинну загаданного слова
    else:
        if len_word >= number and number > 0:
            return True
        else:
            return False


def check_answer(word):
    """Функция проверки введенных символов"""
    while True:
        answer = input("==>> ")
        # проверяем просят ли подсказку
        if answer.isdigit():
            # проверяем что выбранный номер буквы которою хочет открыть пользователь не превышает длинны слова
            if check_number(len_word=len(word), number=int(answer)):
                return int(answer)
            else:
                print("Введен неверный номер буквы")
        else:
            return answer
    
    
def play():
    """функция игры"""
    
    
    # выбираем категорию слова
    category = choice(CATEGORIES.show_categories())
    # список названных букв
    writed_letters = []
    print(f'''     
                                Давайте поиграем в угадайку слов
                                Слово из категории {category}
                                ''')

    
    # загаданное слово
    word = choice(WORDS.show_words(category))
    # строка, содержащая символы _ на каждую букву задуманного слова
    letters = '_' * len(word)  
    # количество попыток
    tries = 6  
    # количество подсказок
    tips = 3
    # выводим висилицу на экран
    print(display_hangman(tries))

    while True:
        # выводим загаданное слово в виде ____
        print(letters)
        print(f'''
                                    введите букву или слово целиком
                                    если желаете подсказку напишите номер буквы которую хотите открыть
                                    ''')
        letter = check_answer(word)

        if type(letter) is int:
            if tips > 0:
                index = letter - 1
                letters = letters[:index] + word[index] + letters[index + 1:]
                
                tips -= 1
                if tips == 1:
                    print("осталась", tips, "подсказка")
                elif tips == 0:
                    print("осталось", tips, "подсказок")
                else:
                    print('осталось', tips, 'подсказки')

            else:
                print('извините у вас больше нет подсказок')

        else:
            tries -= 1
            # проверяем что такая буква не названа
            if letter in writed_letters:
                print('                  Вы уже называли букву', letter)
                
            # проверяем что не ввели правильное слово
            elif letter == word:
                print(f'''
                                         Поздравляем вы угадали слово
                                         Желаете сыграть ещё? да/нет
                                         ''')
                play_yet() 
                break
            
            elif letter in word:
                letter_index = word.index(letter)
                letters = letters[:letter_index] + word[letter_index] + letters[letter_index + 1:]
                
                print("                                     Поздровляем вы угадали букву :=)")
                
                
            
            # если не осталось попыток
            elif tries == 0:
                print(f'''
                                   Вы проиграли, загаданное слово {letter},
                                   {display_hangman(tries)}
                                   Желаете сыграть ещё? да/нет
                          ''')
                play_yet() 
                break

            # если есть попытки но не угадали букву
            else:
                writed_letters.append(letter)
                print(f'''
                                   Вы не угадали, осталось попыток {tries} {display_hangman(tries)}
                                   введите букву или слово целиком из категории {category}
                                   если желаете подсказку напишите номер буквы которую хотите открыть
                      ''')
                
                

def play_yet():
    """функция для вопроса хочет ли рользователь сыграть еще"""
    while True:
        answer = input()
        if not answer.isdigit() and  answer.lower() in ["да", "д", "нет", "не", "н"]:
            if answer.lower() in ["нет", "не", "н"]:
                goodbye()
                break
            else:
                play()      
        else:
            print("             Введена неверная команда")   
            print("             Желаете сыграть ещё? да/нет")   


def goodbye():
    """функция прощания"""
    message = """
                            Всего хорошего, приходите ещё"""
    print(message)



if __name__ == "__main__":
    main()
