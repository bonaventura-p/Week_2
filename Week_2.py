
#turtle basic
from turtle import *

color('red','yellow')
shape('turtle')


begin_fill()

while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
