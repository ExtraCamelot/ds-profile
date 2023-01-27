from random import randint

# ИСКЛЮЧЕНИЯ
#общий клас, содержащий все исключения
class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Указаны координаты вне игрового поля!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "Снаряд в одну и ту же воронку дважды не падет!"

#исключение для правильного положения кораблей
class BoardWrongShipException(BoardException):
    def __str__(self):
        pass


class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # метод сравнения Python
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # метод текстового представления в Python
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"

class Ship:
    def __init__(self, bow, l, o):
        self.bow = bow
        self.l = l
        self.o = o
        self.lives = l

    @property
    def dots(self):
        # точки, из которых состоит корабль
        ship_dots = []
        for i in range(self.l):
           cur_x = self.bow.x
           cur_y = self.bow.y

           if self.o == 0:
               cur_x += i
           elif self.o == 1:
               cur_y += i

           ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots

class Board:
    def __init__(self, hid=False, size=6):
        self.hid = hid
        self.size = size
        self.count = 0
        # изначальное состояние
        self.field = [["0"] * size for _ in range(size)]
        # список стрелянных координат
        self.busy = []
        # список кораблей
        self.ships = []

    # ВЫВОД ДОСКИ
    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i + 1} | " + " | ".join(row) + " |"

        if self.hid:
            res = res.replace("■", "O")
        return res

    # находится ли точка за предалами доски
    def out(self, d):
        return not ((0 <= d.x < self.size) and (0 <= d.y < self.size))

    # В списке near точки вокруг заданной точки
    def contour(self, ship, verb=False):
        near = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 0), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]
        for d in ship.dots:
            for dx, dy in near:
                # сдвиг исходной точки
                cur = Dot(d.x + dx, d.y + dy)
                # self.field()
                if not(self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.x][cur.y] = "."
                    self.busy.append(cur)

    # добавить корабль
    def add_ship(self, ship):
        # проверка что корабль в границе
        for d in ship.dots:
            if self.out(d) or d in self.busy:
                raise BoardWrongShipException()
        # на место точки корабля поставит квадрат
        for d in ship.dots:
            self.field[d.x][d.y] = "■"
            self.busy.append(d)

        self.ships.append(ship)
        self.contour(ship)

    # выстрел - ход игрока
    def shot(self, d):
        if self.out(d):
            raise BoardOutException()

        if d in self.busy:
            raise BoardUsedException()

        self.busy.append(d)

        for ship in self.ships:
            if ship.shooten(d):
                ship.lives -= 1
                self.field[d.x][d.y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[d.x][d.y] = "."
        print("Мимо!")
        return False

    # обнуляем список и теперь храним в нём точки, в которые стрелял игрок
    def begin(self):
        self.busy = []

    def defeat(self):
        return self.count == len(self.ships)


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {d.x + 1} {d.y + 1}")
        return d


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            x, y = cords

            if not (x.isdigit()) or not (y.isdigit()):
                print(" Введите числа! ")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    # конструктор генерации досок для игроков
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hid = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def try_board(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        # расстановка кораблей
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l, randint(0, 1))
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    # метод гарантированно генерирующий случайную доску с кораблями
    def random_board(self):
        board = None
        while board is None:
            board = self.try_board()
        return board

    def greet(self):
        print("--------------------")
        print("  Добро пожаловать  ")
        print("       в игру       ")
        print("     Морской бой    ")
        print("--------------------")
        print("  формат ввода: x y ")
        print("  x - номер строки  ")
        print("  y - номер столбца ")

    def print_boards(self):
        print("-" * 20)
        print("Доска пользователя:")
        print(self.us.board)
        print("-" * 20)
        print("Доска компьютера:")
        print(self.ai.board)
        print("-" * 20)

    # игровой цикл
    def loop(self):
        num = 0
        while True:
            self.print_boards()
            if num % 2 == 0:
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("Ходит компьютер!")
                repeat = self.ai.move()

            if repeat:
                num -= 1

            if self.ai.board.defeat():
                self.print_boards()
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.defeat():
                self.print_boards()
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    # Запускающая функция
    def start(self):
        self.greet()
        self.loop()

g = Game()
g.start()