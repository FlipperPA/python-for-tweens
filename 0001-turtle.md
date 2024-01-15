# Play with Turtle

* Documentation: https://docs.python.org/3/library/turtle.html

```python
import turtle
import random

turtle.bgcolor('black')  # Choose a background color!
turtle.colormode(255)
turtle.speed(0)
for x in range(500):
    r,b,g=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    turtle.pencolor(r,g,b)
    turtle.fd(x+50)
    turtle.rt(91)  # Try changing the "right-turn" angle here!
turtle.exitonclick()
```

```python
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
```

## Pentagon and Star

What is 360 divided by 5 (one for each side?)

```python
import turtle

for x in range(0, 5):
    turtle.fd(200)
    turtle.rt(72)

turtle.done()
```

What happens when we multiple that times two?

```python
import turtle

for x in range(0, 5):
    turtle.fd(200)
    turtle.rt(144)

turtle.done()
```

## A Twelve Petal Flower

```python
import turtle

turtle.title("Twelve Petal Flower")
turtle.setworldcoordinates(-2000, -2000, 2000, 2000)


def draw_flower(x, y, tilt, radius):
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.seth(tilt - 45)
    turtle.circle(radius, 90)
    turtle.left(90)
    turtle.circle(radius, 90)


for tilt in range(0, 360, 30):
    # Loop around all 360 degrees, 30 degrees at a time.
    # This will create 12 petals, because 360 / 30 == 12.
    draw_flower(0, 0, tilt, 1000)
```
