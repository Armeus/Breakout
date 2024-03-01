from turtle import Turtle
from blocks import Blocks

ALIGNMENT = 'center'
FONT = ('Courier', 30, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 5
        self.update_scoreboard()

    # Update scoreboard with new lives and score values
    def update_scoreboard(self):
        self.clear()
        self.goto(0, 250)
        self.write(self.score, align=ALIGNMENT, font=FONT)
        self.goto(-300, 250)
        self.write(f'Lives={self.lives}', align=ALIGNMENT, font=FONT)

    # Increase score by the value of the block that was hit
    def increase_score(self, block):
        self.score += block.point_value
        self.update_scoreboard()

    # Decrease lives by 1
    def decrease_lives(self):
        self.lives -= 1
        self.update_scoreboard()
