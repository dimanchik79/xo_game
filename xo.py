from tkinter import Toplevel


class PlayProcces:
    playstate = False
    x_or_o = "X"


class MainWindow:
    def __init__(self, title, size, shift, root):
        self.title, self.size, self.shift = title, size, shift
        self.root = root
        self.root.title(f'{self.title}')
        self.root.geometry(f'{self.size}{self.shift}')
        self.root.resizable(False, False)


class ChildWindow:
    def __init__(self, title, size, shift, parent_window):
        self.title, self.size, self.shift, self.parent_window = title, size, shift, parent_window
        self.child = Toplevel(parent_window)
        self.child.title(f'{self.title}')
        self.child.geometry(f'{self.size}{self.shift}')


class Players:
    def __init__(self, name, xo, winscount):
        self.name, self.xo, self.winscount = name, xo, winscount


class Board:
    def __init__(self, cell, winn, player):
        self.cell = cell
        self.winn = winn
        self.player = player

    def check_players_win(self):
        if self.cell[0][0] == self.player and self.cell[0][1] == self.player and self.cell[0][2] == self.player:
            self.winn = self.player

        elif self.cell[1][0] == self.player and self.cell[1][1] == self.player and self.cell[1][2] == self.player:
            self.winn = self.player

        elif self.cell[2][0] == self.player and self.cell[2][1] == self.player and self.cell[2][2] == self.player:
            self.winn = self.player

        elif self.cell[0][0] == self.player and self.cell[1][0] == self.player and self.cell[2][0] == self.player:
            self.winn = self.player

        elif self.cell[0][1] == self.player and self.cell[1][1] == self.player and self.cell[2][1] == self.player:
            self.winn = self.player

        elif self.cell[0][2] == self.player and self.cell[1][2] == self.player and self.cell[2][2] == self.player:
            self.winn = self.player

        elif self.cell[0][0] == self.player and self.cell[1][1] == self.player and self.cell[2][2] == self.player:
            self.winn = self.player

        elif self.cell[0][2] == self.player and self.cell[1][1] == self.player and self.cell[2][0] == self.player:
            self.winn = self.player

        else:
            if all(self.cell[0]) and all(self.cell[1]) and all(self.cell[2]):
                self.winn = 3


class DrowXO:
    def __init__(self, x_position, y_position, color, battlefild):
        self.battlefild = battlefild
        self.x_position = x_position
        self.y_position = y_position
        self.color = color

    def drow_x(self):
        self.battlefild.create_line(self.x_position, self.y_position,
                                    self.x_position + 100, self.y_position + 100, fill=self.color)
        self.battlefild.create_line(self.x_position + 100, self.y_position,
                                    self.x_position, self.y_position + 100, fill=self.color)

    def drow_o(self):
        self.battlefild.create_oval(self.x_position, self.y_position,
                                    self.x_position + 100, self.y_position + 100, outline=self.color)
