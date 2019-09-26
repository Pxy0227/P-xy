import turtle
turtle.setup(700 , 500 , 80 , 80)
 
#国旗底
turtle.up()
turtle.goto(-200,200)
turtle.down()
turtle.begin_fill()
turtle.fillcolor("red")
turtle.pencolor("red")
for i in range(2):
    turtle.fd(330)
    turtle.right(90)
    turtle.fd(220)
    turtle.right(90)
turtle.end_fill()

#星星
turtle.up()
turtle.seth(0)
turtle.fd(55)
turtle.seth(-90)
turtle.fd(22)
turtle.seth(-72)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.fd(58)
    turtle.right(144)
turtle.end_fill()

#小星星1
turtle.penup()
turtle.seth(0)
turtle.fd(66)
turtle.seth(-162)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.fd(20)
    turtle.right(144)
turtle.end_fill()

#小星星2
turtle.penup()
turtle.seth(-90)
turtle.fd(22)
turtle.seth(18)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.fd(20)
    turtle.right(144)
turtle.end_fill()

#小星星3
turtle.penup()
turtle.seth(-90)
turtle.fd(20)
turtle.seth(0)
turtle.fd(11)
turtle.seth(-78)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.fd(20)
    turtle.right(144)
turtle.end_fill()

#小星星4
turtle.penup()
turtle.seth(-90)
turtle.fd(40)
turtle.seth(180)
turtle.fd(30)
turtle.seth(58)
turtle.pendown()
turtle.color('yellow')
turtle.begin_fill()
for i in range(5):
    turtle.fd(20)
    turtle.right(144)
turtle.end_fill()
turtle.penup()

turtle.ht()#隐藏箭头


