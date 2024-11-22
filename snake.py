from turtle import Turtle, Screen
LEFT=180
RIGHT=0
UP=90
DOWN=270
STARTING_POSITION=[[0,0],[-20,0],[-60,0]]

class Snake:

    def __init__(self):
        self.segments=[]
        self.setpositions()
        self.head=self.segments[0]

    def setpositions(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
    def add_segment(self,position):
            tim=Turtle("square")
            tim.color("red")
            tim.speed('fastest')
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def reset(self):
        for i in self.segments:
            i.goto(1000,1000)
        self.segments.clear()
        self.setpositions()
        self.head = self.segments[0]
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.fd(20)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def dn(self):
        if self.head.heading() != UP :
            self.head.setheading(270)