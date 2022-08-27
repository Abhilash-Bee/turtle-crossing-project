from turtle import Turtle


class Mothi(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.hideturtle()
        self.goto(0, -270)
        self.setheading(90)
        self.showturtle()

    def move_up(self):
        self.forward(10)
