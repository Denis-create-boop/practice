# тест по языку Python и его фреймворкам, а также по ООП
from main import *
from questions import questions

num = len(questions)
# список ответов пользователя
list_answers = []
# количество ответов пользователя
answers = 0

question = 1
mistakes = 0

wron = 1

# переменная счетчика вопросов и после определенного количества меняеться цвет фона
total = 0
# создаем возможные цвета фона
colors = [
    (204, 204, 214),
    (203, 153, 153),
    (200, 160, 160),
    (190, 150, 150),
    (200, 180, 180),
    (197, 233, 202),
    (239, 154, 154),
    (236, 122, 64),
    (229, 53, 57),
]

count = 0
# переменные текущего цвета
time_color1 = colors[total]
time_color2 = colors[total]
time_color3 = colors[total]
time_color4 = colors[total]
# переменная для какой вариан выбрал пользователь
user_answer = ""


# функция для ознакомления пользователя с правилами
def rules():
    """Функция для ознакомления с правилами прохождения данного теста"""

    # устанавливаем стили текста
    Text = pg.font.SysFont("gabriola", 30)
    h_one = pg.font.SysFont("constantia", 40)

    # выыодим тексты на экран
    info_rules = h_one.render("Ознакомтесь с правилами теста:", True, color_text)
    info_rules_rect = info_rules.get_rect(center=(W / 2, H / 2 - 200))

    inf_text_1 = Text.render(
        "1:  на вопросы отвечать честно и не пользоваться интернетом", True, color_ans
    )
    inf_text_rect = inf_text_1.get_rect(center=(W / 2 - 35, H / 2 - 90))

    info_text_2 = Text.render(
        "2:  на прохождение теста вам даёться 3 ошибки", True, color_ans
    )
    info_text_2_rect = info_text_2.get_rect(center=(W / 2 - 110, H / 2 - 60))

    info_text_3 = Text.render(
        "3:  выбирайте ответ с помощью мыши или цифры указанной рядом с вариантом",
        True,
        color_ans,
    )
    info_text_3_rect = info_text_3.get_rect(center=(W / 2 + 50, H / 2 - 30))

    info_text_4 = Text.render(
        '4:  после выбора варианта ответа нажмите клавишу "ENTER"', True, color_ans
    )
    info_text_4_rect = info_text_4.get_rect(center=(W / 2 - 42, H / 2))

    text_luck = Text.render("Удачи", True, color_ans)
    text_luck_rect = text_luck.get_rect(center=(W / 2, H / 2 + 50))

    # цикл для непрерывного отображения
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    test()
        # заполняем экран всем необходимым
        screen.blit(img_rules, (0, 0))
        screen.blit(info_rules, info_rules_rect)
        screen.blit(inf_text_1, inf_text_rect)
        screen.blit(info_text_2, info_text_2_rect)
        screen.blit(info_text_3, info_text_3_rect)
        screen.blit(info_text_4, info_text_4_rect)
        screen.blit(text_luck, text_luck_rect)
        screen.blit(text_button, text_button_rect)

        pg.display.update()
        clock.tick(fps)


# функция для старта программы
def start():
    """Основная функция для работы с программой"""
    while True:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    rules()

        screen.blit(img_start, (0, 0))
        screen.blit(info_start, (100, 50))
        screen.blit(text_button, text_button_rect)

        pg.display.update()
        clock.tick(fps)


# функция для отображения варианта по нажатию на него мыши и записи результата
def show_mouse_button():
    global user_answer, time_color1, time_color2, time_color3, time_color4, colors, total, wron, answers
    pos = pg.mouse.get_pos()
    #
    # if pos[1] < questions[question][6][1] and pos[1] > questions[question][6][0]:
    #      print("yes 4")
    #      answers += 1
    #      wron = 1

    #      # под каждый вариант проверяем положение мыши и выделяем цветом выбранный вариант
    #      if pos[1] > 270 and pos[1] < 299:
    #           user_answer = 1
    #           time_color1 = (255, 255, 255)
    #           time_color2 = time_color3 = time_color4 = colors[total]
    #           print("1")

    #      elif pos[1] > 300 and pos[1] < 329:
    #           user_answer = 2
    #           time_color2 = (255, 255, 255)
    #           time_color1 = time_color3 = time_color4 = colors[total]
    #           print("2")

    #      elif pos[1] > 330 and pos[1] < 359:
    #           user_answer = 3
    #           time_color3 = (255, 255, 255)
    #           time_color1 = time_color2 = time_color4 = colors[total]
    #           print("3")

    #      elif pos[1] > 360 and pos[1] < 389:
    #           user_answer = 4
    #           time_color4 = (255, 255, 255)
    #           time_color1 = time_color3 = time_color2 = colors[total]
    #           print("4")

    if pos[1] > 265 and pos[1] < 295:
        user_answer = 1
        time_color1 = (255, 255, 255)
        time_color2 = time_color3 = time_color4 = colors[total]
        wron = 0

    elif pos[1] > 300 and pos[1] < 329:
        user_answer = 2
        time_color2 = (255, 255, 255)
        time_color1 = time_color3 = time_color4 = colors[total]
        wron = 0

    elif pos[1] > 330 and pos[1] < 359:
        user_answer = 3
        time_color3 = (255, 255, 255)
        time_color1 = time_color2 = time_color4 = colors[total]
        wron = 0

    elif pos[1] > 360 and pos[1] < 389:
        user_answer = 4
        time_color4 = (255, 255, 255)
        time_color1 = time_color3 = time_color2 = colors[total]
        wron = 0
        print("yes")

    else:
        wron = 0
        user_answer = ""


# функция самого теста
def test():
    """Функция для работы с тестом, отображение вопросов, вариантов ответа и принятия ответа от пользователя"""
    # подключаем все переменные с которыми будем работать
    global answers, count, mistakes, wron, user_answer, colors, total, time_color1, time_color2, time_color3, time_color4, list_answers, ans_one, ans_one_rect, ans_two, ans_two_rect, ans_three, ans_three_rect, ans_four, ans_four_rect, quest, quest_rect, question
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
                    show_mouse_button()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    user_answer = 1
                    time_color1 = (255, 255, 255)
                    time_color2 = colors[total]
                    time_color3 = colors[total]
                    time_color4 = colors[total]
                    if (
                        questions[question][6][0] == 290
                        and questions[question][6][1] == 319
                    ):

                        answers += 1
                        wron = 1
                    else:
                        wron = 0

                elif event.key == pg.K_2:
                    user_answer = 2
                    time_color2 = (255, 255, 255)
                    time_color1 = colors[total]
                    time_color3 = colors[total]
                    time_color4 = colors[total]
                    if (
                        questions[question][6][0] == 320
                        and questions[question][6][1] == 349
                    ):
                        answers += 1
                        wron = 1
                    else:
                        wron = 0

                elif event.key == pg.K_3:
                    user_answer = 3
                    time_color3 = (255, 255, 255)
                    time_color2 = colors[total]
                    time_color1 = colors[total]
                    time_color4 = colors[total]
                    if (
                        questions[question][6][0] == 350
                        and questions[question][6][1] == 379
                    ):
                        answers += 1
                        wron = 1
                    else:
                        wron = 0

                elif event.key == pg.K_4:
                    user_answer = 4
                    time_color4 = (255, 255, 255)
                    time_color2 = colors[total]
                    time_color3 = colors[total]
                    time_color1 = colors[total]
                    if (
                        questions[question][6][0] == 380
                        and questions[question][6][1] == 409
                    ):
                        answers += 1
                        wron = 1
                    else:
                        wron = 0

                elif event.key == pg.K_RETURN:
                    list_answers.append(user_answer)
                    user_answer = ""

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

        text_question = text.render(
            f"вопрос {question}/{len(questions)}", True, color_text
        )
        quest = questions[question][1]
        quest_rect = quest.get_rect(center=(W / 2, H / 2 - 100))

        ans_one = questions[question][2]
        ans_one_rect = ans_one.get_rect(center=(W / 2, H / 2 - 50))
        ans_two = questions[question][3]
        ans_two_rect = ans_two.get_rect(center=(W / 2, H / 2 - 20))
        ans_three = questions[question][4]
        ans_three_rect = ans_three.get_rect(center=(W / 2, H / 2 + 10))
        ans_four = questions[question][5]
        ans_four_rect = ans_four.get_rect(center=(W / 2, H / 2 + 40))

        sf1.fill(time_color1)
        sf2.fill(time_color2)
        sf3.fill(time_color3)
        sf4.fill(time_color4)

        screen.blit(text_question, (1100, 20))
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


# функция для просмотра ошибок
def show_mistakes():
    """функция для отображения правильных ответов о ошибок пользователя"""
    color_answer = (255, 0, 0)
    quest = 1
    # переменная для записи в нее текста который будем выводить на экран
    write_on_screen = ""
    while True:
        # выводим сами вопросы ответ пользователя и правильный ответ
        text_question = text.render(
            f"вопрос {quest}/{len(questions)}", True, color_text
        )
        n = set_position.index(questions[quest][6]) + 2
        text_right = text.render(f"Правильнй ответ:", True, color_text)
        text_answer = text.render(f"Ваш ответ:", True, color_text)
        ttx = text.render(write_on_screen, True, color_text)
        ttx_rect = ttx.get_rect(center=(W / 2, H / 2 + 70))

        # проверяем ответ пользователя если верный выводим верно
        if n - 1 == list_answers[quest - 1]:
            color_answer = (0, 220, 0)
            write_on_screen = "--- Правильно ---"
        # проверяем ответ пользователя если неверный выводим неверно
        else:
            color_answer = (220, 0, 0)
            write_on_screen = "--- Неправильно ---"

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:

                    quest += 1
        # выбираем из словаря вопросы и варианты ответов и записуем в переменные
        quests = questions[quest][1]
        quests_rect = quests.get_rect(center=(W / 2, H / 2 - 150))
        ans_one = questions[quest][2]
        ans_one_rect = ans_one.get_rect(center=(W / 2, H / 2 - 100))
        ans_two = questions[quest][3]
        ans_two_rect = ans_two.get_rect(center=(W / 2, H / 2 - 70))

        ans_three = questions[quest][4]
        ans_three_rect = ans_three.get_rect(center=(W / 2, H / 2 - 40))

        ans_four = questions[quest][5]
        ans_four_rect = ans_four.get_rect(center=(W / 2, H / 2 - 10))

        # выводим на экран переменные которые создали выше
        screen.fill(color_answer)
        screen.blit(text_question, (1100, 20))
        screen.blit(quests, quests_rect)
        screen.blit(ans_one, ans_one_rect)
        screen.blit(ans_two, ans_two_rect)
        screen.blit(ans_three, ans_three_rect)
        screen.blit(ans_four, ans_four_rect)
        screen.blit(ttx, ttx_rect)
        screen.blit(text_right, (200, 505))
        screen.blit(questions[quest][n], (400, 500))
        screen.blit(text_answer, (200, 555))

        # проверяем что пользователь дал ответ на вопрос
        if list_answers[quest - 1] in questions[quest]:
            screen.blit(questions[quest][list_answers[quest - 1] + 1], (400, 550))
        else:
            txt = text.render("нет отета", True, color_text)
            screen.blit(txt, (400, 555))

        pg.display.update()
        clock.tick(fps)


# функция завершения работы программы
def finish(mistakes):
    """Функция для проверки количества ошибок и вывод результата пройден ли тест"""
    while True:
        # создаем переменные которые будем выводить
        if mistakes == 1:
            write_on_screen = "ошыбку"
        elif 1 < mistakes < 5:
            write_on_screen = "ошибки"
        else:
            write_on_screen = "ошибок"

        # формируем возможные тексты вывода результата
        info_tests = text.render(
            f"Вы совершили {mistakes} {write_on_screen} тест не пройден",
            True,
            color_text,
        )
        info_tests_rect = info_tests.get_rect(center=(W / 2, H / 2))
        info_test = text.render(
            f"Поздровляем у вас {answers} правильных ответов из {num}", True, color_text
        )
        info_test_rect = info_test.get_rect(center=(W / 2, H / 2))

        show_answers = text.render("посмотреть свои ответы", True, color_text)
        show_rect = show_answers.get_rect(center=(W / 2, H / 2 + 50))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    loc = pg.mouse.get_pos()
                    print(loc)
                    if (
                        loc[1] <= 645
                        and loc[1] >= 600
                        and loc[0] <= 840
                        and loc[0] >= 560
                    ):
                        show_mistakes()

        # проверяем количество ошибок и выводи результат
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


if __name__ == "__main__":
    start()
