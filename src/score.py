from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 84, "normal")
COLOR = "white"


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.write_score()

    def increase_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(self.position)
        self.write(self.score, False, ALIGNMENT, FONT)


class ScoreBoard:

    def __init__(self, r_position, l_position):
        self.right_board = Score(r_position)
        self.left_board = Score(l_position)

    def increase_right_board(self):
        self.right_board.increase_score()

    def increase_left_board(self):
        self.left_board.increase_score()