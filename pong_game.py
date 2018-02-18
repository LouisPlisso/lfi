# Simple pong game - don't let the ball hit the bottom!
# KidsCanCode - Intro to Programming
from tkinter import *
import random
import time

# Define ball properties and functions
class Ball:
    def __init__(self, canvas, color, size, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, size, size, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.xspeed = random.randrange(-3,3)
        self.yspeed = -1
        self.hit_bottom = False
        self.score = 0

    def draw(self):
        self.canvas.move(self.id, self.xspeed, self.yspeed)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.yspeed = 3
        if pos[3] >= 400:
            self.hit_bottom = True
        if pos[0] <= 0:
            self.xspeed = 3
        if pos[2] >= 500:
            self.xspeed = -3
        if self.hit_paddle(pos) == True:
            self.yspeed = -3
            self.xspeed = random.randrange(-3,3)
            self.score += 1

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False

# Define paddle properties and functions
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.xspeed = 0
        self.speed_factor = 1
        self.canvas.bind_all('<KeyPress-Left>', self.move_left)
        self.canvas.bind_all('<KeyPress-Right>', self.move_right)
        self.canvas.bind_all('<KeyPress-Down>', self.speed_down)
        self.canvas.bind_all('<KeyPress-Up>', self.speed_up)
        self.canvas.bind_all('<KeyPress-space>', self.stop)

    def draw(self):
        self.canvas.move(self.id, self.xspeed, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.xspeed = 0
        if pos[2] >= 500:
            self.xspeed = 0

    def move_left(self, evt):
        self.xspeed = -2 * self.speed_factor
    def move_right(self, evt):
        self.xspeed = 0 * self.speed_factor
    def stop(self, evt):
        # pass just does nothing
        pass
    def speed_up(self, evt):
        self.speed_factor *= 1.2
    def speed_down(self, evt):
        self.speed_factor /= 1.2

def main():
    # Create window and canvas to draw on
    tk = Tk()
    tk.title("Ball Game")
    canvas = Canvas(tk, width=500, height=400, bd=0, bg='papaya whip')
    canvas.pack()
    label = canvas.create_text(5, 5, anchor=NW, text="Score: 0")
    tk.update()
    paddle = Paddle(canvas, 'blue')
    ball = Ball(canvas, 'red', 25, paddle)

    input('hit any key to start')
    # Animation loop
    while ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        canvas.itemconfig(label, text="Score: "+str(ball.score))
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

    # Game Over
    go_label = canvas.create_text(250,200,text="GAME OVER",font=("Helvetica",30))
    tk.update()

if __name__ == '__main__':
    main()
