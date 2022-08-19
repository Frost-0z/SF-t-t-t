def greet():  # Функция приветствия
    print('------------------------')
    print('Приветствуем вас в игре крестики нолики')
    print('Вводите координаты поля через пробел, чтобы сделать ход')
    print('x - номер строки, y - номер столбца')
    print('Первые ходят крестики')
    print('------------------------')


greet()
def convert():
    def show(): #Функция отображения поля
        print(f' 0 1 2')
        for i in range(3):
            print(f'{i}{field[i][0]} {field[i][1]} {field[i][2]}')

    def ask(): #Функция ввода
        while True:
            cords = input('       Ваш ход(x y): ').split()

            if len(cords) != 2:
                print('Введите 2 координаты!')
                continue
            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print('Введите числа!')
                continue

            x, y = int(x), int(y)

            if 0 <= x <= 2 and 0 <= y <= 2:
                if field[x][y] == '-':
                    return x, y
                else:
                    print('Клетка занята!')
            else:
                print('Координаты вне диапазона!')

        return x, y

    def check_win(): #Функция выявления победителя
        win_cords = [((0, 0), (1, 0), (2, 0)),
                     ((0, 0), (0, 1), (0, 2)),
                     ((0, 1), (1, 1), (2, 1)),
                     ((0, 2), (1, 2), (2, 2)),
                     ((1, 0), (1, 1), (1, 2)),
                     ((2, 0), (2, 1), (2, 2)),
                     ((0, 0), (1, 1), (2, 2)),
                     ((0, 2), (1, 1), (2, 0))]
        for cords in win_cords:
            a = cords[0]
            b = cords[1]
            c = cords[2]

            if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != '-':
                print(f'Выиграли - {field[a[0]][a[1]]}!')
                return True
        return False



    num = 0
    field = [#Создаем поле для игры
        ['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']
    ]
    while True:
        num += 1
        show()
        if num % 2 == 1:
            print('Ходит крестик')
        else:
            print('Ходит нолик')

        x, y = ask()

        if num % 2 == 1:
            field[x][y] = 'x'
        else:
            field[x][y] = 'o'

        if check_win():
            show()
            break

        if num == 9:

            print('Победила дружба!')
            show()
            break
            
convert()

n = None
while True:
    n = input('Для продолжения нажмите enter, для выхода - любой символ + enter').lower()
    if n == '':
        convert()
    else:
        break