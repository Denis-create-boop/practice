# главный файл со всеми настройками
import pygame as pg

pg.init()

W, H = 1250, 650

# устанавливаем шрифты
text = pg.font.SysFont("", 25)
text1 = pg.font.SysFont("calibri", 30)
text2 = pg.font.SysFont("couriernew", 25)
text3 = pg.font.SysFont("perpetuaкурсив", 25)

text_mis = pg.font.SysFont("gabriola", 40)
text_start = pg.font.SysFont("candara", 45)

# устанавливаем картинки
img_start = pg.image.load("img/python.jpg")
img_rules = pg.image.load("img/book.jpg")

# устанавливаем фоны
color_fon = (114, 180, 109)
color_text = (78, 46, 52)
color_ans = (10, 50, 50)

# информация на старте
info_start = text_start.render(
    "Добро пожаловать на тест по знанию языка PYTHON", True, (130, 80, 130)
)
text_rect_start = info_start.get_rect(center=(W / 2, H / 2 - 70))

text_button = text.render('для продолжения нажмите "ENTER"', True, (100, 48, 94))
text_button_rect = text_button.get_rect(center=(W / 2, H / 2 + 300))

# устанавливаем размер экрана
screen = pg.display.set_mode((W, H))
fps = 60
clock = pg.time.Clock()


text_test = pg.font.SysFont("aria", 20)

set_position = [(290, 319), (320, 349), (350, 379), (380, 409)]
