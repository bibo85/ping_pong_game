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
border.color('green')
border.begin_fill()
border.goto(-500, 300)
border.goto(500, 300)
border.goto(500, -300)
border.goto(-500, -300)
border.goto(-500, 300)
border.end_fill()

window.mainloop()
