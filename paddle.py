from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 30

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("#0088ff")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_right(self):
        if not self.xcor() > 320:
            new_x = self.xcor() + MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def go_left(self):
        if not self.xcor() < -320:
            new_x = self.xcor() - MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def reset_position(self):
        self.goto(STARTING_POSITION)
