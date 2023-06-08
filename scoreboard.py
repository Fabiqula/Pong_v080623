from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(0, 270)
        self.write(f"{self.l_score}  {self.r_score}", move=False, align='center', font=('Courier', 80, 'normal'))

    def left_scores(self):
        self.l_score += 1
        self.clear()
        self.update_score()
    def right_scores(self):
        self.r_score += 1
        self.clear()
        self.update_score()