import random
import os
from copy import deepcopy
from numpy import transpose

GAME = True


class Game:

    def __init__(self):
        self.empty_cell = ' '
        self.empty_coords_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                                  [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                                  [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                                  [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                                  [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]
        self.field = [[' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ']]
        self.game_mode = 0
        self.valid_coords = (0, 1, 2, 3, 4)

    def start_game(self):

        self.field = [[' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' '],
                      [' ', ' ', ' ', ' ', ' ']]
        while True:
            try:
                self.game_mode = int(input("P vs P - 0, P vs PC - 1: "))
                if self.game_mode == 0:
                    self.game_PVP()
                    break
                elif self.game_mode == 1:
                    self.game_PVC()
                    break
                else:
                    print('Choose valid game mode! (0 / 1)')
            except ValueError:
                print('Choose valid game mode! (0 / 1)')

    def new_game(self):
        while True:
            decision = input('New game? y/n\n')
            if decision == 'y':
                self.clear_empty_coords_list()
                self.start_game()
            elif decision == 'n':
                exit()
            else:
                print('y/n!')
                continue

    def game_PVP(self):
        turn = True
        while not self.check_lose(self.field):
            self.show_field()
            if len(self.empty_coords_list) != 0:
                coords = list(map(int, input(f'turn for {("x" * turn) + ("o" * (not turn))}, enter coordinates [a b]: ').split()))
                if not(coords[0] in self.valid_coords and coords[1] in self.valid_coords):
                    print('Enter valid coords')
                    continue
                if self.make_a_turn(self.field, turn, coords):
                    os.system('CLS')
                    self.empty_coords_list.remove(coords)
                    turn = not turn
                else:
                    os.system('CLS')
                    print('Cell is not empty!')
            else:
                print('Draw!')
                self.new_game()

        print(f'player {("x" * turn) + ("o" * (not turn))} won!')
        self.new_game()

    def game_PVC(self):
        turn = True
        while not self.check_lose(self.field):
            self.show_field()
            if len(self.empty_coords_list) != 0:
                if turn:
                    coords = list(map(int, input(f'turn for {("x" * turn) + ("o" * (not turn))}, enter coordinates: ').split()))
                    if not (coords[0] in self.valid_coords and coords[1] in self.valid_coords):
                        print('Enter valid coords')
                        continue
                else:
                    coords = self.pc_decide()
                if self.make_a_turn(self.field, turn, coords):
                    os.system('CLS')
                    self.empty_coords_list.remove(coords)
                    turn = not turn
                else:
                    os.system('CLS')
                    print('Cell is not empty!')
            else:
                print('Draw!')
                self.new_game()
        print(f'player {("x" * turn) + ("o" * (not turn))} won!')
        self.new_game()

    def make_a_turn(self, field, turn, coords):
        if coords in self.empty_coords_list:
            if field[coords[0]][coords[1]] == ' ':
                field[coords[0]][coords[1]] = ('x' * turn) + ('o' * (not turn))
                return True
        return False

    def pc_decide(self):
        while True:
            mistake_rate = random.randint(0, 1)
            coords = random.choice(self.empty_coords_list)
            temp_field = deepcopy(self.field)
            self.make_a_turn(temp_field, False, coords)
            if not self.check_lose(temp_field) or mistake_rate == 1:
                break
        return coords

    def show_field(self):
        print("ab 0   1   2   3   4 ")
        print(f"0  {self.field[0][0]} | {self.field[0][1]} | {self.field[0][2]} | {self.field[0][3]} | {self.field[0][4]}")
        print("  ___|___|___|___|___")
        print(f"1  {self.field[1][0]} | {self.field[1][1]} | {self.field[1][2]} | {self.field[1][3]} | {self.field[1][4]}")
        print("  ___|___|___|___|___")
        print(f"2  {self.field[2][0]} | {self.field[2][1]} | {self.field[2][2]} | {self.field[2][3]} | {self.field[2][4]}")
        print("  ___|___|___|___|___")
        print(f"3  {self.field[3][0]} | {self.field[3][1]} | {self.field[3][2]} | {self.field[3][3]} | {self.field[3][4]}")
        print("  ___|___|___|___|___")
        print(f"4  {self.field[4][0]} | {self.field[4][1]} | {self.field[4][2]} | {self.field[4][3]} | {self.field[4][4]}")

    def clear_empty_coords_list(self):
        self.empty_coords_list = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4],
                                  [1, 0], [1, 1], [1, 2], [1, 3], [1, 4],
                                  [2, 0], [2, 1], [2, 2], [2, 3], [2, 4],
                                  [3, 0], [3, 1], [3, 2], [3, 3], [3, 4],
                                  [4, 0], [4, 1], [4, 2], [4, 3], [4, 4]]

    def check_pos(self):
        pass

    def check_line(self, field):
        for line in field:
            sett = set(line)
            if sett == {'x'} or sett == {'o'}:
                return True
        return False

    def check_lose(self, field) -> bool:

        diagonal1 = set([field[i][i] for i in range(len(field))])
        diagonal2 = set([field[i][len(field) - i - 1] for i in range(len(field))])
        if self.check_line(field) \
                or self.check_line(transpose(field)) \
                or diagonal1 == {'x'} or diagonal1 == {'o'} \
                or diagonal2 == {'x'} or diagonal2 == {'o'}:
            return True
        return False


Game1 = Game()
Game1.start_game()


