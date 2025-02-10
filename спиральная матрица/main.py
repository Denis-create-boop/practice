
def transform():
    row, col = map(int, input("Введите два числа: ").split())
    matrix = [[0] * col for _ in range(row)]

    # счетчик для вставки
    count = 1

    # левая незаполненная колонка
    col_left = 0
    
    # верхняя незаполненная строка
    row_up = 0

    # правая незаполненная колонка
    col_right = col - 1

    # нижний незаполненный ряд
    row_down = row - 1

    while col_left <= col_right and row_up <= row_down:

        # заполняем верхний ряд
        for i in range(col_left, col_right + 1):
            matrix[col_left][i] = count
            count += 1
        row_up += 1

        # заполняем правый столбец
        for i in range(row_up, row_down + 1):
            matrix[i][col_right] = count
            count += 1
        col_right -= 1
        
        if row_up <= row_down:
            # заполняем нижний ряд
            for i in range(col_right, col_left - 1, -1):
                matrix[row_down][i] = count
                count += 1
            row_down -= 1

        if col_left <= col_right:
            # заполняем левую колонку
            for i in range(row_down, row_up - 1, -1):
                matrix[i][col_left] = count
                count += 1
            col_left += 1

    # выводим матрицу
    for i in range(row):
        for j in range(col):
            print(str(matrix[i][j]).rjust(3), end='')
        print()


if __name__ == "__main__":
    transform()
