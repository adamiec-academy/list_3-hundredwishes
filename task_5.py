from turtle import *

tracer(10)

for i in range(18):
    for j in range(20):
        right(j+10 + i*20)
        forward(80 + j*5)
        penup()
        home()
        pendown()

exitonclick()
