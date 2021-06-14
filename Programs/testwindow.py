from tkinter import *
import random

GAME_WIDTH = 700
GAME_HEIGHT = 700
GAME_SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def change_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

window = Tk()

window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"



window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
print(x)
print(screen_width)
print(window_width)
y = int((screen_height/2) - (window_height/2))
print(y)
print(screen_height)
print(window_height)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# create the window with window_width x window_height
# at the place of x and y

snake = Snake()
food = Food()

window.mainloop()
