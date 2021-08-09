from turtle import Screen, Turtle


class PongField:

    def __init__(self):
        self.line_drawer = Turtle()
        self.field = Screen()
        self.field.bgcolor("black")
        self.field.title("PONG")
        self.field.setup(width=800, height=600)
        self.field.listen()
        self.field.tracer(0)
        self.draw()

    def get_field(self):
        return self.field

    def draw(self):
        self.line_drawer.clear()
        self.line_drawer.color("white")
        self.line_drawer.hideturtle()
        self.line_drawer.penup()
        self.line_drawer.goto((0, -300))
        self.line_drawer.pendown()
        self.line_drawer.goto((0, 300))
