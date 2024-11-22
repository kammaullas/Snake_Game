from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.color('red')
        self.score = 0
        with open("data.txt") as file:
            self.highscore=int(file.read())
        self.goto(0, 270)
        self.write(align="center", font=("Arial", 20, "normal"),arg=f"Score:{self.score:}")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(align="center", font=("Arial", 20, "normal"),arg=f"Score: {self.score} HighScore:{self.highscore:}")
    """
    Commented game_over because of we need to continue the game and keep track of high scores and start updating
    """
    # def game_over(self):
    #     self.goto(-80,0)
    #     self.write(arg="GAME OVER" ,font=("Arial",20,"normal"))
    def reset_score(self):


        if self.score>self.highscore:
            self.highscore=self.score
            with open("data.txt",mode="w") as file:
                file.write(f"{self.highscore}")
        self.score=0
        self.update_scoreboard()
    def increse_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

