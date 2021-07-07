from turtle import Screen
import time

from snake_class import Snake
from food import Food
from score import Score

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

COLLISION_WIDTH = SCREEN_WIDTH/2 - 20
COLLISION_HEIGHT = SCREEN_HEIGHT/2 - 20


class PlaySnakeGame():
    def __init__(self):
        self.score = score = Score()
        self.food = food = Food()
        self.snake = snake = Snake()
        self.screen = Screen()
        self.screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.screen.bgcolor('black')
        self.screen.title('My snake game')
        self.screen.tracer(0)

        self.screen.listen()
        self.screen.onkey(snake.up, 'Up')
        self.screen.onkey(snake.down, 'Down')
        self.screen.onkey(snake.right, 'Right')
        self.screen.onkey(snake.lef, 'Left')
        self.game_is_on = True

    def play(self):
        while self.game_is_on:
            self.screen.update()
            self.snake.move_forward()
            time.sleep(0.08)

            # eat food
            if self.snake.head.distance(self.food) <= 15:
                self.food.random_move()
                self.score.increase_score()
                self.snake.extend()

            # Detect Collision with wall
            if self.snake.head.xcor() > COLLISION_WIDTH \
                    or self.snake.head.xcor() < -COLLISION_WIDTH \
                    or self.snake.head.ycor() > COLLISION_HEIGHT \
                    or self.snake.head.ycor() < -COLLISION_HEIGHT:
                self.game_is_on = False
                self.score.game_over()
                self.screen.exitonclick()

            #     Detect collision with body
            for segment in self.snake.segments[1::]:
                if self.snake.head.distance(segment) < 10:
                    self.game_is_on = False
                    self.score.game_over()
                    self.screen.exitonclick()


play = PlaySnakeGame()
play.play()
