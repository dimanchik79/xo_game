from tkinter import *
from xo import MainWindow, ChildWindow, Players, DrowXO, Board, PlayProcces

global PLAYER_ONE, PLAYER_TWO, CANVA, BOARD
global label_player_one, label_player_two, label_playerone_wins, label_playertwo_wins


def get_settings():
    childwindow = ChildWindow(title="Насройки", size="400x200", shift="+200+350", parent_window=mainwindow.root)
    Label(childwindow.child, text="Игрок №1 (имя)", font=("Courier", "14")).place(x=10, y=10)
    player_one_name = Entry(childwindow.child, width=34, font=("Ariel", "14"))
    player_one_name.insert(0, PLAYER_ONE.name)
    player_one_name.place(x=10, y=40)
    Label(childwindow.child, text="Игрок №2 (имя)", font=("Courier", "14")).place(x=10, y=70)
    player_two_name = Entry(childwindow.child, width=34, font=("Ariel", "14"))
    player_two_name.insert(0, PLAYER_TWO.name)
    player_two_name.place(x=10, y=100)
    Button(childwindow.child, text="Принять", command=lambda: (
        set_players_settings(childwindow.child, player_one_name.get(), player_two_name.get()))).place(x=160, y=160)
    player_one_name.focus_set()


def set_players_settings(window, playerone, playertwo):
    PLAYER_ONE.name = playerone
    PLAYER_TWO.name = playertwo
    window.destroy()


def lets_play():
    global label_player_one, label_player_two, label_playerone_wins, label_playertwo_wins, BOARD
    BOARD = Board(cell=[[0, 0, 0], [0, 0, 0], [0, 0, 0]], player=0, winn=0)
    PlayProcces.playstate = True
    PlayProcces.x_or_o = "X"
    CANVA.delete("all")
    for xy_pos in range(0, 511, 10):
        CANVA.create_line(166, 0, 166, xy_pos, fill="yellow")
        CANVA.create_line(332, 0, 332, xy_pos, fill="yellow")
        CANVA.create_line(0, 166, xy_pos, 166, fill="yellow")
        CANVA.create_line(0, 332, xy_pos, 332, fill="yellow")
        CANVA.update()
    label_player_one = Label(text=f"Игрок: {PLAYER_ONE.name} (X)", fg="dark green", width=22)
    label_player_one.place(x=50, y=5)
    label_playerone_wins = Label(text=f"Побед: {PLAYER_ONE.winscount}", fg="dark green", width=22)
    label_playerone_wins.place(x=50, y=25)
    label_player_two = Label(text=f"Игрок: {PLAYER_TWO.name} (O)", width=22)
    label_player_two.place(x=390, y=5)
    label_playertwo_wins = Label(text=f"Побед: {PLAYER_TWO.winscount}", width=22)
    label_playertwo_wins.place(x=390, y=25)


def press_button(event):
    if not PlayProcces.playstate:
        return

    # Первый ряд
    if (event.x in range(0, 165)) and (event.y in range(0, 165)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[0][0] == 0:
        x_object = DrowXO(x_position=30, y_position=30, color="green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[0][0] = 1
        change_player_o()
    elif (event.x in range(0, 165)) and (event.y in range(0, 165)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[0][0] == 0:
        x_object = DrowXO(x_position=30, y_position=30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[0][0] = 2
        change_player_x()
    elif (event.x in range(166, 331)) and (event.y in range(0, 165)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[0][1] == 0:
        x_object = DrowXO(x_position=166 + 30, y_position=30, color="dark green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[0][1] = 1
        change_player_o()
    elif (event.x in range(166, 331)) and (event.y in range(0, 165)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[0][1] == 0:
        x_object = DrowXO(x_position=166 + 30, y_position=30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[0][1] = 2
        change_player_x()
    elif (event.x in range(332, 500)) and (event.y in range(0, 165)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[0][2] == 0:
        x_object = DrowXO(x_position=332 + 30, y_position=30, color="dark green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[0][2] = 1
        change_player_o()
    elif (event.x in range(332, 500)) and (event.y in range(0, 165)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[0][2] == 0:
        x_object = DrowXO(x_position=332 + 30, y_position=30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[0][2] = 2
        change_player_x()

    # Второй ряд
    elif (event.x in range(0, 165)) and (event.y in range(166, 331)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[1][0] == 0:
        x_object = DrowXO(x_position=30, y_position=166 + 30, color="green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[1][0] = 1
        change_player_o()
    elif (event.x in range(0, 165)) and (event.y in range(166, 331)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[1][0] == 0:
        x_object = DrowXO(x_position=30, y_position=166 + 30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[1][0] = 2
        change_player_x()
    elif (event.x in range(166, 331)) and (event.y in range(166, 331)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[1][1] == 0:
        x_object = DrowXO(x_position=166 + 30, y_position=166 + 30, color="dark green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[1][1] = 1
        change_player_o()
    elif (event.x in range(166, 331)) and (event.y in range(166, 331)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[1][1] == 0:
        x_object = DrowXO(x_position=166 + 30, y_position=166 + 30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[1][1] = 2
        change_player_x()
    elif (event.x in range(332, 500)) and (event.y in range(165, 332)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[1][2] == 0:
        x_object = DrowXO(x_position=332 + 30, y_position=165 + 30, color="dark green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[1][2] = 1
        change_player_o()
    elif (event.x in range(332, 500)) and (event.y in range(165, 332)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[1][2] == 0:
        x_object = DrowXO(x_position=332 + 30, y_position=165 + 30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[1][2] = 2
        change_player_x()

    # Третий ряд
    elif (event.x in range(0, 165)) and (event.y in range(332, 500)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[2][0] == 0:
        x_object = DrowXO(x_position=30, y_position=332 + 30, color="green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[2][0] = 1
        change_player_o()
    elif (event.x in range(0, 165)) and (event.y in range(332, 500)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[2][0] == 0:
        x_object = DrowXO(x_position=30, y_position=332 + 30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[2][0] = 2
        change_player_x()
    elif (event.x in range(166, 331)) and (event.y in range(332, 500)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[2][1] == 0:
        x_object = DrowXO(x_position=166 + 30, y_position=332 + 30, color="dark green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[2][1] = 1
        change_player_o()
    elif (event.x in range(166, 331)) and (event.y in range(332, 500)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[2][1] == 0:
        x_object = DrowXO(x_position=166 + 30, y_position=332 + 30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[2][1] = 2
        change_player_x()
    elif (event.x in range(332, 500)) and (event.y in range(332, 500)) and (PlayProcces.x_or_o == "X") \
            and BOARD.cell[2][2] == 0:
        x_object = DrowXO(x_position=332 + 30, y_position=332 + 30, color="dark green", battlefild=CANVA)
        x_object.drow_x()
        BOARD.cell[2][2] = 1
        change_player_o()
    elif (event.x in range(332, 500)) and (event.y in range(332, 500)) and (PlayProcces.x_or_o == "O") \
            and BOARD.cell[2][2] == 0:
        x_object = DrowXO(x_position=332 + 30, y_position=332 + 30, color="red", battlefild=CANVA)
        x_object.drow_o()
        BOARD.cell[2][2] = 2
        change_player_x()
    BOARD.player = 1
    BOARD.check_players_win()
    if BOARD.winn == 1:
        print_player_wins(player=PLAYER_ONE.name, color="green")
        PLAYER_ONE.winscount += 1
    BOARD.player = 2
    BOARD.check_players_win()
    if BOARD.winn == 2:
        print_player_wins(player=PLAYER_TWO.name, color="red")
        PLAYER_TWO.winscount += 1
    if BOARD.winn == 3:
        print_player_wins(player="НИЧЬЯ!!!", color="yellow")


def print_player_wins(player, color):
    if player == "НИЧЬЯ!!!":
        CANVA.create_text(250, 200, text=f"{player}", fill=color, font=("Impact", "48"))
        return
    CANVA.create_text(250, 200, text=f"{player}", fill=color, font=("Impact", "48"))
    CANVA.create_text(250, 300, text="ПОБЕДИЛ!!!", fill=color, font=("Impact", "48"))


def change_player_o():
    label_player_one.config(foreground="black")
    label_playerone_wins.config(foreground="black")
    label_player_two.config(foreground="red")
    label_playertwo_wins.config(foreground="red")
    PlayProcces.x_or_o = "O"


def change_player_x():
    label_player_one.config(foreground="green")
    label_playerone_wins.config(foreground="green")
    label_player_two.config(foreground="black")
    label_playertwo_wins.config(foreground="black")
    PlayProcces.x_or_o = "X"


if __name__ == "__main__":
    PLAYER_ONE = Players(name="Игрок1", xo="X", winscount=0)
    PLAYER_TWO = Players(name="Игрок2", xo="O", winscount=0)
    mainwindow = MainWindow(title="XO", size="600x600", shift="+100+100", root=Tk())
    mainmenu = Menu(mainwindow.root)
    mainwindow.root.config(menu=mainmenu)
    mainmenu = Menu(mainwindow.root)
    mainwindow.root.config(menu=mainmenu)
    xomenu = Menu(mainmenu, tearoff=0)
    mainmenu.add_cascade(label='Настройки', command=get_settings)
    mainmenu.add_cascade(label='Новая игра', command=lets_play)
    mainmenu.add_cascade(label='Выход', command=lambda: mainwindow.root.destroy())
    CANVA = Canvas(height=500, width=500, background="black")
    CANVA.place(x=50, y=50)
    CANVA.bind("<ButtonPress>", press_button)
    mainwindow.root.mainloop()
