Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Turtle()
t.shape("turtle")
lista = []
color = input("색상 #1을 입력하시오: ")
색상 #1을 입력하시오: yellow
color = input("색상 #2을 입력하시오: ")
색상 #2을 입력하시오: red
color = input("색상 #3을 입력하시오: ")
색상 #3을 입력하시오: blue
t.fillcolor(lista[0])
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t.fillcolor(lista[0])
IndexError: list index out of range
t.fillcolor("tellow"))
SyntaxError: unmatched ')'
t.fillcolor("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(100, 0)
t.down()
t.fillcolor("red")
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.goto(200, 0)
t.down()
t.fillcolor("blue")
t.begin_fill()
t.circle(50)
t.end_fill()
t._screen.exitonclick()
