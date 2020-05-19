import turtle 
import os
import time
wn= turtle.Screen()
wn.title("pong by @saurav tanwar")
wn.bgcolor("black")
wn.setup(width=800, height= 600)
wn.tracer(0)


def gameOver():

    wn2= turtle.Screen()
    wn2.title("pong by @saurav tanwar")
    wn2.bgcolor("black")
    wn2.setup(width=600, height= 500)
    wn2.resetscreen()
    wn.tracer(0)
    pen1 = turtle.Turtle()
    pen1.speed(0)
    pen1.color("white")
    pen1.penup()
    pen1.hideturtle()
    pen1.goto(0,0)
    pen1.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center", font=("courier",24, "normal"))
   
    time.sleep(5) 

      




#score
score_a =0
score_b = 0


#paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid =5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)


#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid =5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 3.5
ball.dy = -3.5

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0",align="center", font=("courier",24, "normal"))

#Functions
def paddle_a_up():
    y= paddle_a.ycor()
    y+=30
    paddle_a.sety(y)

def paddle_a_down():
    y= paddle_a.ycor()
    y-=30
    paddle_a.sety(y)


def paddle_b_up():
    y= paddle_b.ycor()
    y+=30
    paddle_b.sety(y)


def paddle_b_down():
    y= paddle_b.ycor()
    y-=30
    paddle_b.sety(y)

#keybord binding
wn.listen()
wn.onkeypress(paddle_a_up,"w")  
wn.onkeypress(paddle_a_down,"s")   
wn.onkeypress(paddle_b_up,"i")  
wn.onkeypress(paddle_b_down,"k")  

#main game loop
a = True
while a:
    wn.update()



    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # ball border checking for y-axix
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
        os.system("afplay bounce.wav&")

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
        os.system("afplay bounce.wav&")   
#for x cordinator
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx*= -1  
        score_a +=1  
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center", font=("courier",24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx*= -1
        score_b+=1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center", font=("courier",24, "normal"))     

#border checking for paddle_a 
    if paddle_a.ycor()> 250:
        paddle_a.goto(-350,250)

    if paddle_a.ycor()< -250:
        paddle_a.goto(-350,-250)   

#border checking for paddle_b
    if paddle_b.ycor()> 250:
        paddle_b.goto(350,250)

    if paddle_b.ycor()< -250:
        paddle_b.goto(350,-250)         

    #paddle and ball collision
    if (ball.xcor()> 340 and ball.xcor()< 350) and (ball.ycor()< paddle_b.ycor()+50 and ball.ycor()> paddle_b.ycor() -50):
        ball.setx(340)   
        ball.dx *= -1 
        os.system("afplay bounce.wav&")    

    if (ball.xcor()< -340 and ball.xcor()> -350) and (ball.ycor()< paddle_a.ycor()+50 and ball.ycor()> paddle_a.ycor() -50):
        ball.setx(-340)   
        ball.dx *= -1 
        os.system("afplay bounce.wav&")        


    if score_a ==10 or score_b ==10:
       
        gameOver()
        a= False