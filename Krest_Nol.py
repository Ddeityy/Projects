def intro():
    print("***********************")
    print("I      Крестики       I")
    print("I          -          I")
    print("I       Нолики        I")
    print("***********************")

def print_pole():
    print()
    print(f"   | 0 | 1 | 2 | x")
    print("****************")
    for i, row in enumerate(pole):
        row_string = f" {i} | {' | '.join(row)} | "
        print(row_string)
        print("****************")
    print(" y")
    print("")

def user_input():
    while True:
        coord = input("Ваш ход! Введите координаты X и Y: ").split()

        if len(coord) != 2 or len(coord) >=3:
            print("Неправильное кол-во координат")
            continue

        x, y = coord

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if x > 2 or y > 2:
            print("Координаты вне диапазона")
            continue


        if pole[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y

def check_win():
    win_conditions = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in win_conditions:
        symbols = []
        for c in coord:
            symbols.append(pole[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print_pole()
            print("Выиграл X")
            return True
        if symbols == ["O", "O", "O"]:
            print_pole()
            print("Выиграл O")
            return True
    return False


#Крестики-Нолики

intro()

pole = [[" ", " ", " "] for i in range(3)]

round_counter = 0

while True:
    round_counter += 1

    print_pole()

    if round_counter % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = user_input()

    if round_counter % 2 == 1:
        pole[x][y] = "X"
    else:
        pole[x][y] = "O"

    if check_win():
        break

    if round_counter == 9:
        print("Ничья")
        break
