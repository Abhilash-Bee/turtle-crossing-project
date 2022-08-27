import turtle
from turtle import Turtle
from color_data import colour_list
from random import choice, randint
turtle.colormode(255)


class Car:

    def __init__(self):
        self.car_list = []

    def create_car(self):
        car_on = randint(1, 6)
        if car_on == 1:
            new_car = Turtle("square")
            new_car.color(choice(colour_list))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y_rand = randint(-200, 200)
            new_car.penup()
            new_car.goto(300, y_rand)
            self.car_list.append(new_car)

    def move(self):
        for cars in self.car_list:
            cars.backward(5)

