# -*- coding: utf-8 -*-

import turtle
from random import choice, randint

# размеры игрового поля
PLAYING_FIELD_WIDTH = 1000
PLAYING_FIELD_HEIGHT = 600

# размер рокеток в условных единицах. Размер умножается на 10 пикс.
HEIGHT_ROCKET = 6  # это половина высоты рокетки. Реальный размер x2
WIDTH_ROCKET = 1  # этополовина ширины рокетки. Реальный размер x2
ROCKETS_INDENT = 50  # отступ рокеток от края игрового поля в пикс


def move_up_left_rocket():
    y = rocket_left.ycor() + 10
    if y > (PLAYING_FIELD_HEIGHT / 2 - HEIGHT_ROCKET * 10):
        y = PLAYING_FIELD_HEIGHT / 2 - HEIGHT_ROCKET * 10
    rocket_left.sety(y)


def move_down_left_rocket():
    y = rocket_left.ycor() - 10
    if y < (-PLAYING_FIELD_HEIGHT / 2 + HEIGHT_ROCKET * 10):
        y = -PLAYING_FIELD_HEIGHT / 2 + HEIGHT_ROCKET * 10
    rocket_left.sety(y)


def move_up_right_rocket():
    y = rocket_right.ycor() + 10
    if y > (PLAYING_FIELD_HEIGHT / 2 - HEIGHT_ROCKET * 10):
        y = PLAYING_FIELD_HEIGHT / 2 - HEIGHT_ROCKET * 10
    rocket_right.sety(y)


def move_down_right_rocket():
    y = rocket_right.ycor() - 10
    if y < (-PLAYING_FIELD_HEIGHT / 2 + HEIGHT_ROCKET * 10):
        y = -PLAYING_FIELD_HEIGHT / 2 + HEIGHT_ROCKET * 10
    rocket_right.sety(y)


# настройка игрового окна
window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width=1.0, height=1.0)
window.bgcolor('black')

# рисуем игровое поле
border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-PLAYING_FIELD_WIDTH / 2, PLAYING_FIELD_HEIGHT / 2)
border.goto(PLAYING_FIELD_WIDTH / 2, PLAYING_FIELD_HEIGHT / 2)
border.goto(PLAYING_FIELD_WIDTH / 2, -PLAYING_FIELD_HEIGHT / 2)
border.goto(-PLAYING_FIELD_WIDTH / 2, -PLAYING_FIELD_HEIGHT / 2)
border.goto(-PLAYING_FIELD_WIDTH / 2, PLAYING_FIELD_HEIGHT / 2)
border.end_fill()

# рисуем центральную линию
border.goto(0, PLAYING_FIELD_HEIGHT / 2)
border.color('white')
border.setheading(270)
for i in range(PLAYING_FIELD_HEIGHT // 10):
    if i % 2 == 0:
        border.forward(10)
    else:
        border.up()
        border.forward(10)
        border.down()

border.hideturtle()

# рисуем рокетки
rocket_left = turtle.Turtle()
rocket_left.color('white')
rocket_left.shape('square')
rocket_left.shapesize(stretch_len=WIDTH_ROCKET, stretch_wid=HEIGHT_ROCKET)
rocket_left.penup()
rocket_left.goto(-PLAYING_FIELD_WIDTH / 2 + ROCKETS_INDENT, 0)

rocket_right = turtle.Turtle()
rocket_right.color('white')
rocket_right.shape('square')
rocket_right.shapesize(stretch_len=WIDTH_ROCKET, stretch_wid=HEIGHT_ROCKET)
rocket_right.penup()
rocket_right.goto(PLAYING_FIELD_WIDTH / 2 - ROCKETS_INDENT, 0)

# заставляем рокетки двигаться вниз-вверх
window.listen()
window.onkeypress(move_up_left_rocket, 'w')
window.onkeypress(move_down_left_rocket, 's')
window.onkeypress(move_up_right_rocket, 'Up')
window.onkeypress(move_down_right_rocket, 'Down')

# рисуем мячик
ball = turtle.Turtle()
ball.shape('circle')
ball.color('red')
ball.up()
ball.speed(0)
# задаем скорость мячика
ball.dx = choice([-4, -3, -2, 2, 3, 4])
ball.dy = choice([-4, -3, -2, 2, 3, 4])

# движение мяча
while True:
    window.update()

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # касание мяча верхней границы игрового поля
    if ball.ycor() >= PLAYING_FIELD_HEIGHT // 2 - 10:
        ball.dy = -ball.dy
    # касание мяча нижней границы игрового поля
    if ball.ycor() <= -PLAYING_FIELD_HEIGHT // 2 + 10:
        ball.dy = -ball.dy
    # касание мяча правой границы игрового поля
    if ball.xcor() >= PLAYING_FIELD_WIDTH // 2 - 10:
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])
    # касание мяча левой границы игрового поля
    if ball.xcor() <= -PLAYING_FIELD_WIDTH // 2 + 10:
        ball.goto(0, randint(-150, 150))
        ball.dx = choice([-4, -3, -2, 2, 3, 4])
        ball.dy = choice([-4, -3, -2, 2, 3, 4])

window.mainloop()
