from turtle import Turtle

STARTING_POSITION = (250, 0)
MOVE_SPEED = 1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#999999")
        self.penup()
        self.goto(STARTING_POSITION)
        self.x_move = MOVE_SPEED
        self.y_move = MOVE_SPEED

    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.x_move = MOVE_SPEED