from turtle import Turtle

ROW_COLORS = ('blue', 'green', 'yellow', 'orange', 'red',)
START_X = -370

class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.x = START_X
        self.y = 50
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        for color in ROW_COLORS:
            self.x = START_X
            self.create_row(color)
            self.y += 25

    def create_row(self, color):
        for _ in range(12):
            new_block = Turtle('square')
            new_block.color(color)
            new_block.shapesize(stretch_wid=1, stretch_len=3)
            new_block.penup()
            new_block.goto(self.x, self.y)
            self.blocks.append(new_block)
            self.x += 66
