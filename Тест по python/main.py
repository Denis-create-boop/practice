# тест по языку Python и его фреймворкам, а также по ООП
import pygame as pg

pg.init()

W, H = 1400, 740

text = pg.font.SysFont('', 30)
text1 = pg.font.SysFont('calibri', 35)
text2 = pg.font.SysFont('couriernew', 30)
text3 = pg.font.SysFont('perpetuaкурсив', 30)

text_mis = pg.font.SysFont('gabriola', 40)
text_start = pg.font.SysFont('candara', 45)

img_start = pg.image.load('img/python.webp')
img_rules = pg.image.load('img/book.jpg')

color_fon = (114, 180, 109)
color_text = (78, 46, 52)
color_ans = (10, 50, 50)

info_start = text_start.render(
    'Добро пожаловать на тест по знанию языка PYTHON', True, (130, 80, 130))
text_rect_start = info_start.get_rect(center=(W/2, H/2 - 70))

text_button = text.render(
    'для продолжения нажмите "ENTER"', True, (100, 48, 94))
text_button_rect = text_button.get_rect(center=(W/2, H/2 + 300))

screen = pg.display.set_mode((W, H))
fps = 60
clock = pg.time.Clock()


text_test = pg.font.SysFont('aria', 20)

set_position = [(290, 319), (320, 349), (350, 379), (380, 409)]

questions = {1: {1: text1.render('что такое "int"?', True, color_text),
                 2: text2.render('1: функция для определения строковых значений    ', True, color_ans),
                 3: text2.render('2: функция для создания списка                   ', True, color_ans),
                 4: text2.render('3: функция для определения целочисленных значений', True, color_ans),
                 5: text2.render('4: функция для определения вещественных чисел    ', True, color_ans),
                 6: set_position[2]},
             2: {1: text1.render('что такое "print"?', True, color_text),
                 2: text2.render('1: функция для считывания данных с клавиатуры', True, color_ans),
                 3: text2.render('2: функция для вывода данных на экран        ', True, color_ans),
                 4: text2.render('3: переменная для определения словаря        ', True, color_ans),
                 5: text2.render('4: функция для сортировки                    ', True, color_ans),
                 6: set_position[1]},
             3: {1: text1.render('"input" это:', True, color_text),
                 2: text2.render('1: переменная', True, color_ans),
                 3: text2.render('2: функция   ', True, color_ans),
                 4: text2.render('3: условие   ', True, color_ans),
                 5: text2.render('', True, color_ans),
                 6: set_position[1]},
             4: {1: text1.render('для чего нужна функция "input"?', True, color_text),
                 2: text2.render('1: для вывода данных      ', True, color_ans),
                 3: text2.render('2: для создания множества ', True, color_ans),
                 4: text2.render('3: для определения функции', True, color_ans),
                 5: text2.render('4: для ввода данных       ', True, color_ans),
                 6: set_position[3]},
             5: {1: text1.render('какая функция может читать строку как математическое выражение?', True, color_text),
                 2: text2.render('1: path()  ', True, color_ans),
                 3: text2.render('2: string()', True, color_ans),
                 4: text2.render('3: eval()  ', True, color_ans),
                 5: text2.render('4: alight()', True, color_ans),
                 6: set_position[2]},
             6: {1: text1.render('что такое "end"?', True, color_text),
                 2: text2.render('1: функция для создания условий              ', True, color_ans),
                 3: text2.render('2: функция для создания окончаний            ', True, color_ans),
                 4: text2.render('3: функция для расстановки пробелов для строк', True, color_ans),
                 5: text2.render('4: функция для вычесления корня              ', True, color_ans),
                 6: set_position[1]},
             7: {1: text1.render('что такое "str"?', True, color_text),
                 2: text2.render('1: функция для создания строки            ', True, color_ans),
                 3: text2.render('2: метод для создания строки              ', True, color_ans),
                 4: text2.render('3: символ для создия строки               ', True, color_ans),
                 5: text2.render('4: переменная для создания и записи строки', True, color_ans),
                 6: set_position[0]},
             8: {1: text1.render('"float" это:', True, color_text),
                 2: text2.render('1: функция для определения строки             ', True, color_ans),
                 3: text2.render('2: функция для определения целого числа       ', True, color_ans),
                 4: text2.render('3: функция для определения вещественного числа', True, color_ans),
                 5: text2.render('', True, color_ans),
                 6: set_position[2]},
             9: {1: text1.render('что делает "floor"?', True, color_text),
                 2: text2.render('1: находит индекс элемента          ', True, color_ans),
                 3: text2.render('2: округляет число по значению вниз ', True, color_ans),
                 4: text2.render('3: округляет число по значению вверх', True, color_ans),
                 5: text2.render('4: такой функции нет в Python       ', True, color_ans),
                 6: set_position[1]},
             10: {1: text1.render('какой метод подсчитывает количество пересекающихся вложений строки?', True, color_text),
                  2: text2.render('1: count()', True, color_ans),
                  3: text2.render('2: title()', True, color_ans),
                  4: text2.render('3: total()', True, color_ans),
                  5: text2.render('4: lower()', True, color_ans),
                  6: set_position[0]},
             11: {1: text1.render('"if" это:', True, color_text),
                  2: text2.render('1: это переменная             ', True, color_ans),
                  3: text2.render('2: "if" не относиться к Python', True, color_ans),
                  4: text2.render('3: условное выражение         ', True, color_ans),
                  5: text2.render('4: функция для создания списка', True, color_ans),
                  6: set_position[2]},
             12: {1: text1.render('какой метод в классе автоматически вызываеться сразу после метода "__new__"?', True, color_text),
                  2: text3.render('1: __name__ ', True, color_ans),
                  3: text3.render('2: ___doc___', True, color_ans),
                  4: text3.render('3: __init___', True, color_ans),
                  5: text3.render('4: __slots__', True, color_ans),
                  6: set_position[2]},
             13: {1: text1.render('с помощью какой функции можно перебрать все элементы массива без цикла "for"?', True, color_text),
                  2: text2.render('1: map()   ', True, color_ans),
                  3: text2.render('2: lambda()', True, color_ans),
                  4: text2.render('3: filter()', True, color_ans),
                  5: text2.render('4: set()   ', True, color_ans),
                  6: set_position[0]},
             14: {1: text1.render('с помощью какого ключевого слова можно унаследовать один шаблон html от другого?', True, color_text),
                  2: text2.render('1: super   ', True, color_ans),
                  3: text2.render('2: daughter', True, color_ans),
                  4: text2.render('3: section ', True, color_ans),
                  5: text2.render('4: extends ', True, color_ans),
                  6: set_position[3]},
             15: {1: text1.render('Как правильно создавать условие в Jinja?              ', True, color_text),
                  2: text2.render('1: с помощью одинарных фигурных скобок: {}            ', True, color_ans),
                  3: text2.render('2: с помощью двойных фигурных скобок: {{}}            ', True, color_ans),
                  4: text2.render('3: с помощью одинарных фигурных скобок и знака %: {%%}', True, color_ans),
                  5: text2.render('4: с помощью знака %: %                               ', True, color_ans),
                  6: set_position[2]},
             16: {1: text1.render('"middle" это:', True, color_text),
                  2: text2.render('1: функция для нахождения суммы чисел      ', True, color_ans),
                  3: text2.render('2: функция для нахождения модуля           ', True, color_ans),
                  4: text2.render('3: функция для нахождения степени          ', True, color_ans),
                  5: text2.render('4: функция для нахождения среднего значения', True, color_ans),
                  6: set_position[3]},
             17: {1: text1.render('"for" это:', True, color_text),
                  2: text2.render('1: условный оператор', True, color_ans),
                  3: text2.render('2: множество        ', True, color_ans),
                  4: text2.render('3: переменная       ', True, color_ans),
                  5: text2.render('4: цикл             ', True, color_ans),
                  6: set_position[3]},
             18: {1: text1.render('выберите правильное написание функции', True, color_text),
                  2: text2.render('1: def funk():  n = 5 return print(n)', True, color_ans),
                  3: text2.render('2: def funk(x): if x is int: return x', True, color_ans),
                  4: text2.render('3: def funk: x = 2 return x          ', True, color_ans),
                  5: text2.render('4: def funk(x) print(X)              ', True, color_ans),
                  6: set_position[1]},
             19: {1: text1.render('что делает метод "title"?', True, color_text),
                  2: text2.render('1: возводит первый символ каждого слова в строке в нижний регистр ', True, color_ans),
                  3: text2.render('2: возводит последний символ каждого слова в нижний регистр       ', True, color_ans),
                  4: text2.render('3: возводит первый символ каждого слова в строке в верхний регистр', True, color_ans),
                  5: text2.render('4: возводит последний символ каждого слова в верхний регистр      ', True, color_ans),
                  6: set_position[2]},
             20: {1: text1.render('с помощью какого метода можно добавлять элементы во множества?', True, color_text),
                  2: text2.render('1: add()    ', True, color_ans),
                  3: text2.render('2: pop()    ', True, color_ans),
                  4: text2.render('3: discard()', True, color_ans),
                  5: text2.render('4: clear()  ', True, color_ans),
                  6: set_position[0]},
             21: {1: text1.render('как создать короткую однострочную функцию?', True, color_text),
                  2: text2.render('1: lambda x: x if x > 0', True, color_ans),
                  3: text2.render('2: funk x: return x    ', True, color_ans),
                  4: text2.render('3: def x: return x     ', True, color_ans),
                  5: text2.render('4: lambda x: return x  ', True, color_ans),
                  6: set_position[0]},
             22: {1: text1.render('что такое "sep"?', True, color_text),
                  2: text2.render('1: функция для создания условий              ', True, color_ans),
                  3: text2.render('2: функция для создания окончаний            ', True, color_ans),
                  4: text2.render('3: функция для расстановки пробелов для строк', True, color_ans),
                  5: text2.render('4: функция для вычесления корня              ', True, color_ans),
                  6: set_position[2]},
             23: {1: text1.render('с помощью какой функции можно определять код символа в таблице "unicode"?', True, color_text),
                  2: text2.render('1: ord() ', True, color_ans),
                  3: text2.render('2: chr() ', True, color_ans),
                  4: text2.render('3: drow()', True, color_ans),
                  5: text2.render('4: num() ', True, color_ans),
                  6: set_position[0]},
             24: {1: text1.render('что делает метод "isalpha()"?', True, color_text),
                  2: text2.render('1: проверяет состоит ли строка только из пробелов          ', True, color_ans),
                  3: text2.render('2: проверяет состоит ли строка только из буквенных символов', True, color_ans),
                  4: text2.render('3: проверяет состоит ли строка из символов                 ', True, color_ans),
                  5: text2.render('4: проверяет является ли строка не пустой                  ', True, color_ans),
                  6: set_position[1]},
             25: {1: text1.render('что такое macro в Jinja?', True, color_text),
                  2: text2.render('1: функция представления                                     ', True, color_ans),
                  3: text2.render('2: функция списка                                            ', True, color_ans),
                  4: text2.render('3: ключевое слово для создания словаря                       ', True, color_ans),
                  5: text2.render('4: ключевое слово для создания некой функции ("def" в python)', True, color_ans),
                  6: set_position[3]},
             26: {1: text1.render('для чего нужна функция "max"?', True, color_text),
                  2: text2.render('1: для определения максимального значения', True, color_ans),
                  3: text2.render('2: для определения минимального значения ', True, color_ans),
                  4: text2.render('3: для вычесления корня                  ', True, color_ans),
                  5: text2.render('4: для умножения числа на строку         ', True, color_ans),
                  6: set_position[0]},
             27: {1: text1.render('"and" это:', True, color_text),
                  2: text2.render('1: оператор логического умножения', True, color_ans),
                  3: text2.render('2: функция                       ', True, color_ans),
                  4: text2.render('3: переменная                    ', True, color_ans),
                  5: text2.render('', True, color_ans),
                  6: set_position[0]},
             28: {1: text1.render('что делает "sqrt"?', True, color_text),
                  2: text2.render('1: вычесляет квадратный корень      ', True, color_ans),
                  3: text2.render('2: вычесляет абсолютный модуль числа', True, color_ans),
                  4: text2.render('3: находит среднее значение         ', True, color_ans),
                  5: text2.render('', True, color_ans),
                  6: set_position[0]},
             29: {1: text1.render('как правильно прописывать строковые методы?', True, color_text),
                  2: text2.render('1: строка(метод) ', True, color_ans),
                  3: text2.render('2: метод.строка  ', True, color_ans),
                  4: text2.render('3: метод(строка) ', True, color_ans),
                  5: text2.render('4: строка.метод()', True, color_ans),
                  6: set_position[3]},
             30: {1: text1.render('с помощью какого модуля можно генерировать случайные числа?', True, color_text),
                  2: text2.render('1: turtle', True, color_ans),
                  3: text2.render('2: math  ', True, color_ans),
                  4: text2.render('3: string', True, color_ans),
                  5: text2.render('4: random', True, color_ans),
                  6: set_position[3]},
             31: {1: text1.render('что делает метод "items()"?', True, color_text),
                  2: text2.render('1: возвращает кортеж из пары ключ, значение', True, color_ans),
                  3: text2.render('2: добавляет в словарь новое значение      ', True, color_ans),
                  4: text2.render('3: разширяет словарь другим словарём       ', True, color_ans),
                  5: text2.render('4: возвращает ключи словаря                ', True, color_ans),
                  6: set_position[0]},
             32: {1: text1.render('с помощью чего можно создать бесконечный цикл?', True, color_text),
                  2: text2.render('1: while True:    ', True, color_ans),
                  3: text2.render('2: self True:     ', True, color_ans),
                  4: text2.render('3: for True:      ', True, color_ans),
                  5: text2.render('4: def while True:', True, color_ans),
                  6: set_position[0]},
             33: {1: text1.render('"not" это:', True, color_text),
                  2: text2.render('1: словарь             ', True, color_ans),
                  3: text2.render('2: условный оператор   ', True, color_ans),
                  4: text2.render('3: логическое отрицание', True, color_ans),
                  5: text2.render('4: переменная          ', True, color_ans),
                  6: set_position[2]},
             34: {1: text1.render('с помощью какого тега можно создавать ссылки в html?', True, color_text),
                  2: text2.render('1: <ol> ', True, color_ans),
                  3: text2.render('2: <p>  ', True, color_ans),
                  4: text2.render('3: <a>  ', True, color_ans),
                  5: text2.render('4: <img>', True, color_ans),
                  6: set_position[2]},
             35: {1: text1.render('как правильно подключать модуль "math"?', True, color_text),
                  2: text2.render('1: connect math                     ', True, color_ans),
                  3: text2.render('2: from Python import math          ', True, color_ans),
                  4: text2.render('3: import math                      ', True, color_ans),
                  5: text2.render('4: модуль "math" не нужно подключать', True, color_ans),
                  6: set_position[2]},
             36: {1: text1.render('что делает метод "isdigit()"?', True, color_text),
                  2: text2.render('1: проверяет состоит ли строка только из букв                   ', True, color_ans),
                  3: text2.render('2: проверяет состоит ли строка только из цивр                   ', True, color_ans),
                  4: text2.render('3: проверяет состоит ли строка только из букв в верхнем регистре', True, color_ans),
                  5: text2.render('4: проверяет состоит ли строка только из букв в нижнем регистре ', True, color_ans),
                  6: set_position[1]},
             37: {1: text1.render('выберите правильный вызов функции "funk(x=1, *args, **kwargs)":', True, color_text),
                  2: text2.render('1: funk(1, 2, 3, x=5)           ', True, color_ans),
                  3: text2.render('2: funk(x=0, 5, 6, 0, z=15, w=2)', True, color_ans),
                  4: text2.render('3: funk(y=5 : z=10)             ', True, color_ans),
                  5: text2.render('4: funk(a)                      ', True, color_ans),
                  6: set_position[1]},
             38: {1: text1.render('что делает "ceil"?', True, color_text),
                  2: text2.render('1: находит индекс элемента          ', True, color_ans),
                  3: text2.render('2: округляет число по значению вниз ', True, color_ans),
                  4: text2.render('3: округляет число по значению вверх', True, color_ans),
                  5: text2.render('4: такой функции нет в Python       ', True, color_ans),
                  6: set_position[2]},
             39: {1: text1.render('выберите метакласс из списка:', True, color_text),
                  2: text2.render('1: class()', True, color_ans),
                  3: text2.render('2: type() ', True, color_ans),
                  4: text2.render('3: meta() ', True, color_ans),
                  5: text2.render('4: try()  ', True, color_ans),
                  6: set_position[1]},
             40: {1: text1.render('"zip()" это:', True, color_text),
                  2: text2.render('1: функция которая возвращает True или False             ', True, color_ans),
                  3: text2.render('2: функция для открытия файла                            ', True, color_ans),
                  4: text2.render('3: функция для обьединения отдельных элементов из каждой ', True, color_ans),
                  5: text2.render('  переданной последовательности в кортежи                ', True, color_ans),
                  6: set_position[2]},
             41: {1: text1.render('что делает метод "split()"?', True, color_text),
                  2: text2.render('1: разширяет список другим списком                                  ', True, color_ans),
                  3: text2.render('2: удаляет переданный в него элемент из списка                      ', True, color_ans),
                  4: text2.render('3: разбивает строку на слова используя в качестве разделителя пробел', True, color_ans),
                  5: text2.render('4: удаляет элемент из списка                                        ', True, color_ans),
                  6: set_position[2]},
             42: {1: text1.render('как называеться таблица кодировки символов?', True, color_text),
                  2: text2.render('1: AISIC', True, color_ans),
                  3: text2.render('2: ASCII', True, color_ans),
                  4: text2.render('3: ASICI', True, color_ans),
                  5: text2.render('4: ACSII', True, color_ans),
                  6: set_position[1]},
             43: {1: text1.render('"math" это:', True, color_text),
                  2: text2.render('1: множество', True, color_ans),
                  3: text2.render('2: словарь  ', True, color_ans),
                  4: text2.render('3: функция  ', True, color_ans),
                  5: text2.render('4: модуль   ', True, color_ans),
                  6: set_position[3]},
             44: {1: text1.render('выберите правильный синтаксис написания функции "for"', True, color_text),
                  2: text2.render('1: for range in(2):       ', True, color_ans),
                  3: text2.render('2: for i in range(2):     ', True, color_ans),
                  4: text2.render('3: for i in not range(2): ', True, color_ans),
                  5: text2.render('4: for i in self.range(2):', True, color_ans),
                  6: set_position[1]},
             45: {1: text1.render('какой метод возводит строку в верхний регистр?', True, color_text),
                  2: text2.render('1: hight()   ', True, color_ans),
                  3: text2.render('2: upletter()', True, color_ans),
                  4: text2.render('3: lower()   ', True, color_ans),
                  5: text2.render('4: upper()   ', True, color_ans),
                  6: set_position[3]},
             46: {1: text1.render('с помощью какого ключевого слова обьявляеться функция?', True, color_text),
                  2: text2.render('1: funk', True, color_ans),
                  3: text2.render('2: new ', True, color_ans),
                  4: text2.render('3: set ', True, color_ans),
                  5: text2.render('4: def ', True, color_ans),
                  6: set_position[3]},
             47: {1: text1.render('"isinstance" это:', True, color_text),
                  2: text2.render('1: функция для получения координат                                    ', True, color_ans),
                  3: text2.render('2: функция для проверки соответствия обьекта к какому-либо типу данных', True, color_ans),
                  4: text2.render('3: функция для проверки являеться ли обьект переданный в неё классом  ', True, color_ans),
                  5: text2.render('   или обьектом класса                                                ', True, color_ans),
                  6: set_position[1]},
             48: {1: text1.render('с помощью какого метода можно обьединять множества?', True, color_text),
                  2: text2.render('1: add()   ', True, color_ans),
                  3: text2.render('2: union() ', True, color_ans),
                  4: text2.render('3: append()', True, color_ans),
                  5: text2.render('4: pop()   ', True, color_ans),
                  6: set_position[1]},
             49: {1: text1.render('с помощью какого метода можно создавать словари с одним значение для всех ключей?', True, color_text),
                  2: text2.render('1: answkeys() ', True, color_ans),
                  3: text2.render('2: values()   ', True, color_ans),
                  4: text2.render('3: fromkeys() ', True, color_ans),
                  5: text2.render('4: frozenset()', True, color_ans),
                  6: set_position[2]},
             50: {1: text1.render('для чего нужна функция "sum"?', True, color_text),
                  2: text2.render('1: для возведения в стерень               ', True, color_ans),
                  3: text2.render('2: для нахождения суммы элементов         ', True, color_ans),
                  4: text2.render('3: для нахождения самаго большого элемента', True, color_ans),
                  5: text2.render('4: для определения математической функции ', True, color_ans),
                  6: set_position[1]},
             51: {1: text1.render('что делает функция "len"?', True, color_text),
                  2: text2.render('1: вычесляет корень           ', True, color_ans),
                  3: text2.render('2: находит длинну обьекта     ', True, color_ans),
                  4: text2.render('3: вычесляет модуль числа     ', True, color_ans),
                  5: text2.render('4: выводит информация на экран', True, color_ans),
                  6: set_position[1]},
             52: {1: text1.render('какой метод возводит строку в нижний регистр?', True, color_text),
                  2: text2.render('1: higth()   ', True, color_ans),
                  3: text2.render('2: upletter()', True, color_ans),
                  4: text2.render('3: lower()   ', True, color_ans),
                  5: text2.render('4: upper()   ', True, color_ans),
                  6: set_position[2]},
             53: {1: text1.render('с помощью какой функции можно создать множество?', True, color_text),
                  2: text2.render('1: dict()', True, color_ans),
                  3: text2.render('2: map() ', True, color_ans),
                  4: text2.render('3: list()', True, color_ans),
                  5: text2.render('4: set() ', True, color_ans),
                  6: set_position[3]},
             54: {1: text1.render('с помощью какой функции можно создать кортеж?', True, color_text),
                  2: text2.render('1: map()  ', True, color_ans),
                  3: text2.render('2: set()  ', True, color_ans),
                  4: text2.render('3: tuple()', True, color_ans),
                  5: text2.render('4: dict() ', True, color_ans),
                  6: set_position[2]},
             55: {1: text1.render('что делает функция "abs"?', True, color_text),
                  2: text2.render('1: вычесляет квадратный корень               ', True, color_ans),
                  3: text2.render('2: вычесляет сумму переданных в неё элементов', True, color_ans),
                  4: text2.render('3: вычисляет радиус окружности               ', True, color_ans),
                  5: text2.render('4: вычесляет модуль числа                    ', True, color_ans),
                  6: set_position[3]},
             56: {1: text1.render('с помощью какой команды можно запустить сервер на django?', True, color_text),
                  2: text2.render('1: python manage.py runserver  ', True, color_ans),
                  3: text2.render('2: python runserver            ', True, color_ans),
                  4: text2.render('3: python django runserver     ', True, color_ans),
                  5: text2.render('4: python manage.py startserver', True, color_ans),
                  6: set_position[0]},
             57: {1: text1.render('на какой диагонали матрицы находяться равные значения?', True, color_text),
                  2: text2.render('1: на побочной             ', True, color_ans),
                  3: text2.render('2: на главной              ', True, color_ans),
                  4: text2.render('3: ansна обеих             ', True, color_ans),
                  5: text2.render('4: у матрицы нет диагоналей', True, color_ans),
                  6: set_position[1]},
             58: {1: text1.render('какую функцию нужно описать в классе для сложения чисел?', True, color_text),
                  2: text3.render('1: __add__', True, color_ans),
                  3: text3.render('2: __sub__ ', True, color_ans),
                  4: text3.render('3: __mul__ ', True, color_ans),
                  5: text3.render('4: __div__ ', True, color_ans),
                  6: set_position[0]},
             59: {1: text1.render('для чего нужна функция "min"?', True, color_text),
                  2: text2.render('1: для определения максимального значения', True, color_ans),
                  3: text2.render('2: для определения минимального значения ', True, color_ans),
                  4: text2.render('3: для вычесления корня                  ', True, color_ans),
                  5: text2.render('4: для умножения числа на строку         ', True, color_ans),
                  6: set_position[1]},
             60: {1: text1.render('"or" это:', True, color_text),
                  2: text2.render('1: такого нет в Python             ', True, color_ans),
                  3: text2.render('2: переменная                      ', True, color_ans),
                  4: text2.render('3: оператор для обьединения условий', True, color_ans),
                  5: text2.render('4: условный оператор               ', True, color_ans),
                  6: set_position[2]},
             61: {1: text1.render('что делает метод "capitalize"?', True, color_text),
                  2: text2.render('1: возводит строку в нижний регистр                  ', True, color_ans),
                  3: text2.render('2: возводит первый символ строки в верхний регистр   ', True, color_ans),
                  4: text2.render('3: возводит последний символ строки в верхний регистр', True, color_ans),
                  5: text2.render('4: возводит строку в верхний регистр                 ', True, color_ans),
                  6: set_position[1]},
             62: {1: text1.render('"list" это:', True, color_text),
                  2: text2.render('1: функция для создания словаря  ', True, color_ans),
                  3: text2.render('2: функция для создания списка   ', True, color_ans),
                  4: text2.render('3: функция для создания множества', True, color_ans),
                  5: text2.render('4: функция для создания кортежа  ', True, color_ans),
                  6: set_position[1]},
             63: {1: text1.render('с помощью какой функции можно определять символ по коду в таблице "unicode"?', True, color_text),
                  2: text2.render('1: sym()', True, color_ans),
                  3: text2.render('2: chr()', True, color_ans),
                  4: text2.render('3: ord()', True, color_ans),
                  5: text2.render('4: num()', True, color_ans),
                  6: set_position[1]},
             64: {1: text1.render('что нужно написать в теле функции что бы она ничего не выполняла?', True, color_text),
                  2: text2.render('1: stop', True, color_ans),
                  3: text2.render('2: None', True, color_ans),
                  4: text2.render('3: pass', True, color_ans),
                  5: text2.render('4: rect', True, color_ans),
                  6: set_position[2]},
             65: {1: text1.render('с помощью какого метода можно разширить один список другим списком?', True, color_text),
                  2: text2.render('1: append()', True, color_ans),
                  3: text2.render('2: extend()', True, color_ans),
                  4: text2.render('3: just()  ', True, color_ans),
                  5: text2.render('4: split() ', True, color_ans),
                  6: set_position[1]},
             66: {1: text1.render('как создать класс?', True, color_text),
                  2: text2.render('1: с помощью ключевого слова "class"', True, color_ans),
                  3: text2.render('2: с помощью ключевого слова "def"  ', True, color_ans),
                  4: text2.render('3: с помощью ключевого слова "call" ', True, color_ans),
                  5: text2.render('4: с помощью метода class()         ', True, color_ans),
                  6: set_position[0]},
             67: {1: text1.render('с помощью какой функции можно проверить к камому типу относиться обьект?', True, color_text),
                  2: text2.render('1: type()', True, color_ans),
                  3: text2.render('2: bool()', True, color_ans),
                  4: text2.render('3: tipe()', True, color_ans),
                  5: text2.render('4: set() ', True, color_ans),
                  6: set_position[0]},
             68: {1: text1.render('какой декоратор разрешает обращаться к переменной только внутри данного класса?', True, color_text),
                  2: text2.render('1: @classmethod ', True, color_ans),
                  3: text2.render('2: @private     ', True, color_ans),
                  4: text2.render('3: @property    ', True, color_ans),
                  5: text2.render('4: @staticmethod', True, color_ans),
                  6: set_position[2]},
             69: {1: text1.render('как создать словарь?', True, color_text),
                  2: text2.render('1: d = set() ', True, color_ans),
                  3: text2.render('2: d = dict  ', True, color_ans),
                  4: text2.render('3: d = set   ', True, color_ans),
                  5: text2.render('4: d = dict()', True, color_ans),
                  6: set_position[3]},
             70: {1: text1.render('с помощью какой функции можно добавлять новые переменные в класс?', True, color_text),
                  2: text2.render('1: hasattr()', True, color_ans),
                  3: text2.render('2: getattr()', True, color_ans),
                  4: text2.render('3: setattr()', True, color_ans),
                  5: text2.render('4: delattr()', True, color_ans),
                  6: set_position[2]},
             71: {1: text1.render('с помощью какого метода можно добавить элемент в конец списка?', True, color_text),
                  2: text2.render('1: append()', True, color_ans),
                  3: text2.render('2: extend()', True, color_ans),
                  4: text2.render('3: just()  ', True, color_ans),
                  5: text2.render('4: split() ', True, color_ans),
                  6: set_position[0]},
             72: {1: text1.render('какой метод выводит набор атрибутов экземпляра класса?', True, color_text),
                  2: text3.render('1: __doc__  ', True, color_ans),
                  3: text3.render('2: __name__', True, color_ans),
                  4: text3.render('3: __init__  ', True, color_ans),
                  5: text3.render('4: __dict__  ', True, color_ans),
                  6: set_position[3]},
             73: {1: text1.render('как в словарях храняться данные?', True, color_text),
                  2: text2.render('1: в виде кортежей      ', True, color_ans),
                  3: text2.render('2: в паре ключ, значение', True, color_ans),
                  4: text2.render('3: элементами списка    ', True, color_ans),
                  5: text2.render('4: в виде переменных    ', True, color_ans),
                  6: set_position[1]},
             74: {1: text1.render('как вызываеться инициализатор родительского класса при наследовании классов?', True, color_text),
                  2: text3.render('1: ___funk___', True, color_ans),
                  3: text2.render('2:mro()  ', True, color_ans),
                  4: text2.render('3:super()', True, color_ans),
                  5: text3.render('4: ___next___', True, color_ans),
                  6: set_position[2]},
             75: {1: text1.render('что делает функция "abs"?', True, color_text),
                  2: text2.render('1: вычесляет квадратный корень               ', True, color_ans),
                  3: text2.render('2: вычесляет сумму переданных в неё элементов', True, color_ans),
                  4: text2.render('3: вычисляет радиус окружности               ', True, color_ans),
                  5: text2.render('4: вычесляет модуль числа                    ', True, color_ans),
                  6: set_position[3]},
             76: {1: text1.render('с помощью какого метода можно сгенерировать исключение?', True, color_text),
                  2: text2.render('1: raice ', True, color_ans),
                  3: text2.render('2: exept ', True, color_ans),
                  4: text2.render('3: finaly', True, color_ans),
                  5: text2.render('4: slots ', True, color_ans),
                  6: set_position[0]},
             77: {1: text1.render('какой командой запускаеться flask?', True, color_text),
                  2: text2.render('1: start', True, color_ans),
                  3: text2.render('2: run  ', True, color_ans),
                  4: text2.render('3: go   ', True, color_ans),
                  5: text2.render('4: play ', True, color_ans),
                  6: set_position[1]},
             78: {1: text1.render('какой метод в регулярных выражениях ищет все вхождения строки?', True, color_text),
                  2: text2.render('1: find()   ', True, color_ans),
                  3: text2.render('2: finder() ', True, color_ans),
                  4: text2.render('3: findall()', True, color_ans),
                  5: text2.render('', True, color_ans),
                  6: set_position[2]},
             79: {1: text1.render('как задать символьный класс в регулярных выражениях?', True, color_text),
                  2: text2.render('1: {} ', True, color_ans),
                  3: text2.render('2: () ', True, color_ans),
                  4: text2.render('3: <> ', True, color_ans),
                  5: text2.render('4: [] ', True, color_ans),
                  6: set_position[3]},
             80: {1: text1.render('с помощью какого метода можно изменять и записывать данные пользователя?', True, color_text),
                  2: text2.render('1: GET() ', True, color_ans),
                  3: text2.render('2: RECT()', True, color_ans),
                  4: text2.render('3: POST()', True, color_ans),
                  5: text2.render('', True, color_ans),
                  6: set_position[2]}

             }

num = len(questions)
list_answers = []

def rules():
    
    Text = pg.font.SysFont('gabriola', 30)
    h_one = pg.font.SysFont('constantia', 40)

    info_rules = h_one.render('Ознакомтесь с правилами теста:', True, color_text)
    info_rules_rect = info_rules.get_rect(center=(W/2, H/2 - 200))

    inf_text_1 = Text.render('1:  на вопросы отвечать честно и не пользоваться интернетом', True, color_ans)
    inf_text_rect = inf_text_1.get_rect(center=(W/2 - 35, H/2 - 90))

    info_text_2 = Text.render('2:  на прохождение теста вам даёться 3 ошибки', True, color_ans)
    info_text_2_rect = info_text_2.get_rect(center=(W/2 - 110, H/2 - 60))

    info_text_3 = Text.render('3:  выбирайте ответ с помощью мыши или цифры указанной рядом с вариантом', True, color_ans)
    info_text_3_rect = info_text_3.get_rect(center=(W/2 + 50, H/2 - 30))

    info_text_4 = Text.render('4:  после выбора варианта ответа нажмите клавишу "ENTER"', True, color_ans)
    info_text_4_rect = info_text_4.get_rect(center=(W/2 - 42, H/2))

    text_luck = Text.render('Удачи', True, color_ans)
    text_luck_rect = text_luck.get_rect(center=(W/2, H/2 + 50))

    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    test()

        #screen.fill(color)
        screen.blit(img_rules, (-280, 0))
        screen.blit(info_rules, info_rules_rect)
        screen.blit(inf_text_1, inf_text_rect)
        screen.blit(info_text_2, info_text_2_rect)
        screen.blit(info_text_3, info_text_3_rect)
        screen.blit(info_text_4, info_text_4_rect)
        screen.blit(text_luck, text_luck_rect)
        screen.blit(text_button, text_button_rect)

        pg.display.update()
        clock.tick(fps)
        

def start():
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    rules()

        
        screen.blit(img_start, (0, 0))
        screen.blit(info_start, (100, 10))
        screen.blit(text_button, text_button_rect)

        pg.display.update()
        clock.tick(fps)

# 72 74 79
answers = 0


def test():
     global answers, list_answers, ans_one, ans_one_rect, ans_two, ans_two_rect, ans_three, ans_three_rect, ans_four, ans_four_rect, quest, quest_rect, question

     colors = [(124, 111, 86), (115, 200, 200), (97, 115, 70), (255, 215, 236), (224, 250, 247), (197, 233, 202), (239, 154, 154),
               (236, 122, 64), (229, 53, 57)]
     question = 1
     mistakes = 0

     wron = 1

     total = 0
     count = 0 
     time_color1 = colors[total]
     time_color2 = colors[total]
     time_color3 = colors[total]
     time_color4 = colors[total]
     ness = ''
     while True:

          sf1 = pg.Surface((1300, 30))
          sf2 = pg.Surface((1300, 30))
          sf3 = pg.Surface((1300, 30))
          sf4 = pg.Surface((1300, 30))

            
          for event in pg.event.get():
               if event.type == pg.QUIT:
                    exit()

               if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                         Y = pg.mouse.get_pos()
                         ness = ''    
                         if Y[1] < questions[question][6][1] and Y[1] > questions[question][6][0]:

                              answers += 1
                              wron = 1

                              if Y[1] > 290 and Y[1] < 319:
                                   ness = 1
                                   time_color1 = (255, 255, 255)
                                   time_color2 = time_color3 = time_color4 = colors[total]     
                              elif Y[1] > 320 and Y[1] < 349:
                                   ness = 2
                                   time_color2 = (255, 255, 255)
                                   time_color1 = time_color3 = time_color4 = colors[total]     
                              elif Y[1] > 350 and Y[1] < 379:
                                   ness = 3
                                   time_color3 = (255, 255, 255)
                                   time_color1 = time_color2 = time_color4 = colors[total]     
                              elif Y[1] > 380 and Y[1] < 409:
                                   ness = 4
                                   time_color4 = (255, 255, 255)
                                   time_color1 = time_color3 = time_color2 = colors[total]     
                         elif Y[1] > 285 and Y[1] < 315:
                              ness = 1
                              time_color1 = (255, 255, 255)
                              time_color2 = time_color3 = time_color4 = colors[total]
                              wron = 0 
                         elif Y[1] > 320 and Y[1] < 349:
                              ness = 2
                              time_color2 = (255, 255, 255)
                              time_color1 = time_color3 = time_color4 = colors[total]
                              wron = 0 
                         elif Y[1] > 350 and Y[1] < 379:
                              ness = 3
                              time_color3 = (255, 255, 255)
                              time_color1 = time_color2 = time_color4 = colors[total]
                              wron = 0 
                         elif Y[1] > 380 and Y[1] < 409:
                              ness = 4
                              time_color4 = (255, 255, 255)
                              time_color1 = time_color3 = time_color2 = colors[total]
                              wron = 0

                         else:
                              wron = 0
                              ness = ''

               elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_1:
                         ness = 1
                         time_color1 = (255, 255, 255)
                         time_color2 = colors[total]
                         time_color3 = colors[total]
                         time_color4 = colors[total]
                         if questions[question][6][0] == 290 and questions[question][6][1] == 319:

                              answers += 1
                              wron = 1
                         else:
                              wron = 0


                    elif event.key == pg.K_2:
                         ness = 2
                         time_color2 = (255, 255, 255)
                         time_color1 = colors[total]
                         time_color3 = colors[total]
                         time_color4 = colors[total]
                         if questions[question][6][0] == 320 and questions[question][6][1] == 349:  
                              answers += 1
                              wron = 1
                         else:
                              wron = 0


                    elif event.key == pg.K_3:
                         ness = 3
                         time_color3 = (255, 255, 255)
                         time_color2 = colors[total]
                         time_color1 = colors[total]
                         time_color4 = colors[total]
                         if questions[question][6][0] == 350 and questions[question][6][1] == 379:  
                              answers += 1
                              wron = 1
                         else:
                              wron = 0


                    elif event.key == pg.K_4:
                         ness = 4
                         time_color4 = (255, 255, 255)
                         time_color2 = colors[total]
                         time_color3 = colors[total]
                         time_color1 = colors[total]
                         if questions[question][6][0] == 380 and questions[question][6][1] == 409:  
                              answers += 1
                              wron = 1
                         else:
                              wron = 0

                    elif event.key == pg.K_RETURN:
                         list_answers.append(ness)
                         ness = ''

                         if question == num:
                              finish(mistakes)
                                  
                         elif wron == 0:
                              mistakes += 1

                         wron = 1
                         question += 1
                         time_color1 = colors[total]
                         time_color2 = colors[total]
                         time_color3 = colors[total]
                         time_color4 = colors[total]

                         if count <= 14:
                              count += 1
                         else:
                              count = 0     
                              if total < 9:
                                   total += 1
                                   time_color1 = colors[total]
                                   time_color2 = colors[total]
                                   time_color3 = colors[total]
                                   time_color4 = colors[total]
                              else:
                                   total = 0
                                   time_color1 = colors[total]
                                   time_color2 = colors[total]
                                   time_color3 = colors[total]
                                   time_color4 = colors[total]

              

          screen.fill(colors[total])

          text_question = text.render(f'вопрос {question}/{len(questions)}', True, color_text) 
          quest = questions[question][1]
          quest_rect = quest.get_rect(center=(W/2, H/2 - 100))

          ans_one = questions[question][2]
          ans_one_rect = ans_one.get_rect(center=(W/2, H/2 - 50))     
          ans_two = questions[question][3]
          ans_two_rect = ans_two.get_rect(center=(W/2, H/2 - 20))     
          ans_three = questions[question][4]
          ans_three_rect = ans_three.get_rect(center=(W/2, H/2 + 10)) 
          ans_four = questions[question][5]
          ans_four_rect = ans_four.get_rect(center=(W/2, H/2 + 40)) 

          sf1.fill(time_color1)
          sf2.fill(time_color2)
          sf3.fill(time_color3)
          sf4.fill(time_color4)

          screen.blit(text_question, (1180, 20))
          screen.blit(quest, quest_rect)     
          sf1.blit(ans_one, (0, 0))
          screen.blit(sf1, ans_one_rect)     
          sf2.blit(ans_two, (0, 0))
          screen.blit(sf2, ans_two_rect)     
          sf3.blit(ans_three, (0, 0))
          screen.blit(sf3, ans_three_rect)   
          sf4.blit(ans_four, (0, 0))
          screen.blit(sf4, ans_four_rect)    
          screen.blit(text_button, text_button_rect)   
          pg.display.update()
          clock.tick(fps)

def show_mistakes():
     color_answer = (255, 0, 0)
     quest = 1
     a = ''
     while True:
          
          text_question = text.render(f'вопрос {quest}/{len(questions)}', True, color_text)
          n = set_position.index(questions[quest][6]) + 2
          text_right = text.render(f'Правильнй ответ:', True, color_text)
          text_answer = text.render(f'Ваш ответ:', True, color_text)
          ttx = text.render(a, True, color_text)
          ttx_rect = ttx.get_rect(center=(W/2, H/2 + 70))
          

          if n - 1  == list_answers[quest - 1]:
               color_answer = (0, 220, 0)
               a = '--- Правильно ---'
          else:
               color_answer = (220, 0, 0)
               a = "--- Неправильно ---"

          for event in pg.event.get():
               if event.type == pg.QUIT:
                    exit()

               if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:

                         quest += 1
                         

          quests = questions[quest][1]
          quests_rect = quests.get_rect(center=(W/2, H/2 - 150))
          ans_one = questions[quest][2]
          ans_one_rect = ans_one.get_rect(center=(W/2, H/2 - 100)) 
          ans_two = questions[quest][3]
          ans_two_rect = ans_two.get_rect(center=(W/2, H/2 - 70))

          ans_three = questions[quest][4]
          ans_three_rect = ans_three.get_rect(center=(W/2, H/2 - 40))

          ans_four = questions[quest][5]
          ans_four_rect = ans_four.get_rect(center=(W/2, H/2 - 10))        
          
          screen.fill(color_answer)
          screen.blit(text_question, (1180, 20))
          screen.blit(quests, quests_rect)
          screen.blit(ans_one, ans_one_rect)
          screen.blit(ans_two, ans_two_rect)
          screen.blit(ans_three, ans_three_rect)
          screen.blit(ans_four, ans_four_rect)
          screen.blit(ttx, ttx_rect)
          screen.blit(text_right, (200, 505))
          screen.blit(questions[quest][n], (400, 500))
          screen.blit(text_answer, (200, 555))
          if list_answers[quest - 1] in questions[quest]:
               screen.blit(questions[quest][list_answers[quest - 1] + 1], (400, 550))
          else:
               txt = text.render("нет отета", True, color_text)
               screen.blit(txt, (400, 555))

          pg.display.update()
          clock.tick(fps)


def finish(mistakes):
     while True:
          if mistakes == 1:
               c = "ошыбку"
          elif 1 < mistakes < 5:
               c = "ошибки"
          else:
               c = "ошибок"
          info_tests = text.render(
              f'Вы совершили {mistakes} {c} тест не пройден', True, color_text)
          info_tests_rect = info_tests.get_rect(center=(W/2, H/2))
          info_test = text.render(
              f'Поздровляем у вас {answers} правильных ответов из {num}', True, color_text)
          info_test_rect = info_test.get_rect(center=(W/2, H/2))

          show_answers = text.render("посмотреть свои ответы", True, color_text)
          show_rect = show_answers.get_rect(center=(W/2, H/2 + 50))

          for event in pg.event.get():
               if event.type == pg.QUIT:
                    exit()

               elif event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                         loc = pg.mouse.get_pos()
                         if loc[1] <= 450 and loc[1] >= 400 and loc[0] <= 840 and loc[0] >= 560:
                              show_mistakes()


          if mistakes > 2:
               screen.fill(color_fon)
               screen.blit(info_tests, info_tests_rect)
               screen.blit(show_answers, show_rect)
               pg.display.update()
               clock.tick(fps)

          else:
               screen.fill(color_fon)
               screen.blit(info_test, info_test_rect)
               screen.blit(show_answers, show_rect)
               pg.display.update()
               clock.tick(fps)



if __name__ == '__main__':
    start()
