
import random


def elements_in_pass(lenth, param):
    elements = ''
    for _ in range(lenth):
        elements += random.choice(param)
    return elements


def check(question, answer):
    if answer.lower() in ["да", "д"]:
        return True
    elif answer.lower() in ["нет", "не", "н"]:
        return False
    else:
        print("Введены неккоректные данные")
        print(question)
        answer = input()
        return check(question, answer)

def main():
    while True:
        result = ''

        while True:
            # длина пароля
            lenth_pass = input("Введите длину пароля: ")
            try:
                lenth_pass = int(lenth_pass)
                break
            except:
                print('Введите число')

        # включать ли цыфры
        question = 'Включать ли цифры в пароль?'
        print(question)
        nums_pass = input()
        if check(question, nums_pass):
            result += elements_in_pass(lenth_pass, "1234567890")

        # включать ли заглавные
        question = 'Включать ли заглавные буквы в пароль?'
        print(question)
        upper_letters = input()
        if check(question, upper_letters):
            result += elements_in_pass(lenth_pass, "QWERTYUIOPASDFGHJKLZXCVBNM")

        # включать ли строчные
        question = 'Включать ли строчные буквы в пароль?'
        print(question)
        lower_letters = input()
        if check(question, lower_letters):
            result += elements_in_pass(lenth_pass, "qwertyuiopasdfghjklzxcvbnm")

        # включать ли символы
        question = 'Включать ли символы в пароль?'
        print(question)
        sym_pass = input()
        if check(question, sym_pass):
            result += elements_in_pass(lenth_pass, ".,_-?!")

        password = random.sample(result, lenth_pass)

        print(f"Пароль сгенерирован, ваш пароль: {''.join(password)}")
        question = "Хотите сгенерировать новый пароль? да/нет"
        print(question)
        answer = input()
        if check(question, answer) == False:
            break


if __name__ == "__main__":
    main()