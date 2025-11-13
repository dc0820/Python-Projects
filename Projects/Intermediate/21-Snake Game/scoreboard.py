from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")
SCORE = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = SCORE
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


    def game_over(self):
        self.goto(x=0, y=270)
        self.clear()
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)