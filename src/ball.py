from turtle import Turtle

COLOR = "white"


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color(COLOR)
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
