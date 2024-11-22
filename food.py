from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.food = 0
        self.pu()
        self.shape("circle")
        self.color("black")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.refresh()
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)
