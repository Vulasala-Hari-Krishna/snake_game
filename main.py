from turtle import Turtle,Screen
from snake import Snake
from food import Food
from score import ScoreBoard
score = ScoreBoard()
import time
game_over = Turtle()
game_over.color("white")
game_over.penup()
game_over.hideturtle()
food = Food()
snake = Snake()
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.tracer(0)
is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.all_segments[0].xcor() > 280 or snake.all_segments[0].xcor() < -280 or snake.all_segments[0].ycor() < -280 or snake.all_segments[0].ycor() > 280:
        game_over.write("Game Over",align="center",font=("Arial",50,"normal"))
        is_game_on = False
    else:
        if snake.all_segments[0].distance(food) < 15:
            food.update()
            score.update()
            snake.extend()
        for segment in snake.all_segments[1:]:
            if snake.all_segments[0].distance(segment) < 10 :
                game_over.write("Game Over", align="center", font=("Arial", 50, "normal"))
                is_game_on = False

screen.exitonclick()