from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.penup()
        self.goto(-270, 250)
        self.score_up()

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score = {self.score}", font=("courier", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align="center", font=("courier", 40, "bold"))
