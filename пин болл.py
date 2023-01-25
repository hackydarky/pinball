import random
import time
from tkinter import *

tk = Tk()
tk.title("игра")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=600)
canvas.pack()
tk.update()


class Ball:
    def __init__(self, canvas, paddle, color):
        self.paddle = paddle
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 250, 250)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        list_a = [-3, -2, -1, 1, 2, 3]
        random.shuffle(list_a)
        self.x = list_a[0]
        self.y = -3
        self.hitbutton = False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hitbutton = True
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2
        if self.hitpaddle(pos) == True:
            self.y = -3

    def hitpaddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                return True
            return False


class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-Left>", self.turn_l)
        self.canvas.bind_all("<KeyPress-Right>", self.turn_r)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        if pos[2] >= self.canvas_width:
            self.x = 0

    def turn_l(self, evt):
        self.x = -2

    def turn_r(self, evt):
        self.x = 2


paddle = Paddle(canvas, "blue")
ball = Ball(canvas, paddle, "red")

while 1:
    if ball.hitbutton == False:
        ball.draw()
        paddle.draw()
    else:
        canvas.create_text(250, 250, text="конец игры :)", font=("Arial", 32))
    tk.update()
    time.sleep(0.01)
