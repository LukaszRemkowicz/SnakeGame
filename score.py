from turtle import Turtle

FONT = ('Courier', 24, 'normal')
ALIGN = 'center'


class Score(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 400)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self) -> None:
        self.write(f'Score: {self.score}', align=ALIGN, font=FONT)

    def increase_score(self) -> None:
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self) -> None:
        self.goto(0, 0)
        self.write('Game is over', align=ALIGN, font=FONT)
