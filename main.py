# -*- coding: utf-8 -*-

import turtle

# настройка игрового окна
window = turtle.Screen()
window.title('Ping-Pong')
window.setup(width=1.0, height=1.0)
window.bgcolor('black')

# размеры игрового поля
playing_field_width = 1000
playing_field_height = 600

# рисуем игровое поле
border = turtle.Turtle()
border.speed(0)
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

# рисуем центральную линию
border.goto(0, 300)
border.color('white')
border.setheading(270)
for i in range(25):
    if i % 2 == 0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()

border.hideturtle()

# рисуем рокетки
rocket_left = turtle.Turtle()
rocket_left.color('white')
rocket_left.shape('square')
rocket_left.shapesize(stretch_len=1, stretch_wid=6)
rocket_left.penup()
rocket_left.goto(-450, 0)

rocket_right = turtle.Turtle()
rocket_right.color('white')
rocket_right.shape('square')
rocket_right.shapesize(stretch_len=1, stretch_wid=6)
rocket_right.penup()
rocket_right.goto(450, 0)

window.mainloop()
