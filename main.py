from turtle import Screen
import time
from car import Car
from mothi_the_turtle import Mothi
from score import Score

screen = Screen()
mothi = Mothi()
car = Car()
score = Score()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
TIME = 0.11
change_time = 0.01


screen.listen()
screen.onkey(fun=mothi.move_up, key="Up")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(TIME - change_time)
    car.create_car()
    car.move()

    if mothi.ycor() >= 290:
        change_time += 0.01
        score.score_up()
        mothi.setposition(0, -270)

    for car_obj in car.car_list:
        if mothi.distance(car_obj) < 25:
            score.game_over()
            is_game_on = False

screen.exitonclick()
