
def transform():
    row, col = map(int, input("Введите два числа: ").split())
    matrix = [[0] * col for _ in range(row)]

    # числа для вставки
    count = 1
    # вспомогательные переменные
    a, b = 0, 0
    # последний незаполненный ряд
    rows = row -1
    # последний незаполненный столбец
    cols = col - 1

    while a <= cols and b <= rows:

        # заполняем верхний ряд
        for i in range(a, cols + 1):
            matrix[a][i] = count
            count += 1
        b += 1

        # заполняем правую колонку
        for i in range(b, rows + 1):
            matrix[i][cols] = count
            count += 1
        cols -= 1

        if b <= rows:
            # заполняем нижний ряд
            for i in range(cols, a - 1, -1):
                matrix[rows][i] = count
                count += 1
            rows -= 1
        
        if a <= cols:
            # заполняем левый столбец
            for i in range(rows, b - 1, -1):
                matrix[i][a] = count
                count += 1
            a += 1

    # выводим матрицу
    for i in range(row):
        for j in range(col):
            print(str(matrix[i][j]).rjust(3), end='')
        print()



if __name__ == "__main__":
    transform()