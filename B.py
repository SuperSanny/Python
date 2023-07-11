from turtle import *
speed(5)
color('green', 'yellow')
begin_fill()
pensize(1)
while True:
    forward(200)
    right(155)
    if abs(pos()) < 1:
        break
end_fill()
done()