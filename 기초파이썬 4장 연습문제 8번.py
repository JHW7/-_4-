Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle
t = turtle.Turtle()
t.shpe("turtle")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.shpe("turtle")
AttributeError: 'Turtle' object has no attribute 'shpe'. Did you mean: 'shape'?
t.shape("turtle")
lista = []
lista.append(int(input("x1: ")))
x1: 0
lista.append(int(input("y1: ")))
y1: 0
lista.append(int(input("x2: ")))
x2: 100
lista.append(int(input("y1: ")))
y1: 0
lista.append(int(input("y2: ")))
y2: 100
lista.append(int(input("x3: ")))
x3: 200
lista.append(int(input("y3: ")))
y3: 100
t.goto(lista[0], lista[1])
t.goto(lista[2], lista[3])
t.goto(lista[4], lista[5])
t._screen.exitonclick()