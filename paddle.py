from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)
        self.y_move_up = 40
        self.y_move_down = -40
    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=0.8, outline=8)
        self.goto(position)


    def stop_up(self):
        self.y_move_up = 0

    def stop_down(self):
        self.y_move_down = 0

    def go_up(self):
        new_y = self.ycor() + self.y_move_up
        self.goto(self.xcor(), new_y)
        self.y_move_down = -40
    def go_down(self):
        new_y = self.ycor() + self.y_move_down
        self.goto(self.xcor(), new_y)
        self.y_move_up = 40

