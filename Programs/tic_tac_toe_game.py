from tkinter import *
import random


def next_turn(row, column):
    global player
    result = ""

    if buttons[row][column]["text"] == "" and check_winner() is False:
        # this one will stop if the game is already ended
        if player == players[0]:

            buttons[row][column]["text"] = player

            if check_winner() is False:
                # check if put there will win or lose in this round
                player = players[1]
                label.config(text=(players[1] + " turn"))

            elif check_winner() is True:
                label.config(text=(players[0] + " wins"))
                result = players[0] + " wins"
            elif check_winner() == "Tie":
                label.config(text="Tie!")
                result = "Tie"

        else:

            buttons[row][column]["text"] = player

            if check_winner() is False:
                # check if put there will win or lose in this round
                player = players[0]
                label.config(text=(players[0] + " turn"))
            elif check_winner() is True:
                label.config(text=(players[1] + " wins"))
                result = players[1] + " wins"
            elif check_winner() == "Tie":
                label.config(text="Tie!")
                result = "Tie"
    else:
        label.config(text=("Game: " + result))


def check_winner():
    # check if there is a horizontal winner
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    # check if there is a vertical winner
    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    # check if there is a diagonal winner
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    # check if there is empty space to continue playing
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False


def empty_spaces():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player

    player = random.choice(players)

    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#F0F0F0")


################## Window Creation #############################
window = Tk()
window.title("Tic-Tac-Toe")
################## Player Initialization #############################
players = ["x", "o"]
player = random.choice(players)
################## Button Creation #############################
# #---------------------------------------------------------------
# pad buttons initialization
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

# ---------------------------------------------------------------
# label creation
label = Label(text=player + " turn",
              font=("consolas", 40))
label.pack(side="top")

# ---------------------------------------------------------------
# reset creation
reset_button = Button(text="restart",
                      font=("consolas", 20),
                      command=new_game)
reset_button.pack(side="top")

# ---------------------------------------------------------------
# frame creation
frame = Frame(window)
frame.pack()

# ---------------------------------------------------------------
# pad buttons creation
for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="",
                                      font=("consolas", 40),
                                      width=5,
                                      height=2,
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

#################################################################
window.mainloop()
