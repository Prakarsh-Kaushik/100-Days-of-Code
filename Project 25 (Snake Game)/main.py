from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Sapola Game")
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_running = True
while game_running:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #Eat Food and Increase Score
    if snake.head.distance(food) < 15:
        food.reposition()
        snake.extend()
        score.increase_score()

    #Game End on Wall Hit
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        score.reset_score()
        snake.reset()
    #Game End on Tail Collision
    for seg in snake.segment_list[1:]:
        if snake.head.distance(seg) < 10:
            score.reset_score()
            snake.reset()





screen.exitonclick()
