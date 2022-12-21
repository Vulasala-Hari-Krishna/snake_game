from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score : {self.score}",align="center",font=("Arial",25,"normal"))
    def update(self):
        self.score+=1
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 25, "normal"))
