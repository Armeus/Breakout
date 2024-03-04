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
        with open('highscore.txt') as highscore:
            self.highscore = int(highscore.read())
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

    # Saves highscore and shows game over screen
    def game_over(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('highscore.txt', mode='w') as highscore:
                highscore.write(f"{self.highscore}")
        text = Turtle()
        text.color('white')
        text.penup()
        text.hideturtle()
        text.goto(0, 0)
        text.write('GAME OVER', align=ALIGNMENT, font=('Courier', 50, 'normal'))
