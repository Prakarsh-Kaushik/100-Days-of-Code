from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(x=150, y=-280)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score - {self.score} | High Score - {self.high_score}", align="center", font=("Arial", 16, "normal"))

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("red")
    #     self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()


