from turtle import exitonclick, goto
from random import randint

mount=[]
for i in range(20): 
    mount.append(randint(0,9) + i*10)

def drawmountain(x):
    for i in range(x):
        for j in range(20):
            goto(5 * j + 200*i, mount[j] + randint(-10,10))
        for h in range(20):
            goto((5 * (h + 19) + i*200), mount[-h-1] + randint(-10,10))

drawmountain(2)
exitonclick()
