import winsound
from time import sleep
import turtle
#in 2d, width is height

print("Loading the screen...")
sleep(2)


window = turtle.Screen()
window.title("                                                                                   PING PONG DING DONG ITS MODERNIZATION")
window.bgcolor("lime")
#scoring
sa = 0
sb = 0


#makes the dimensions, bottom is -300 height, left is -400 width center is 0,0
window.setup(width=800, height=600)


#makes it so that we have to manually update python ourselves
window.tracer(0)

# Program paddle A.
pa = turtle.Turtle() #turtle.Turtle() means creating an object
pa.speed(0)
pa.shape("square")
pa.color("blue")
pa.shapesize(stretch_wid=5, stretch_len=0.5) #when it says 5, it means 5 x (20 original pixels) for the height.
pa.penup() # prevents it from making a line to the nearest object
pa.goto(-350,0)


#Program paddle B

pb = turtle.Turtle() #turtle.Turtle() means creating an object
pb.speed(0)
pb.shape("square")
pb.color("red")
pb.shapesize(stretch_wid=5, stretch_len=0.5) #when it says 5, it means 5 x (20 original pixels) for the height.
pb.penup() #Prevents it from making a line to the nearest object
pb.goto(350,0)



# Program ball

ball = turtle.Turtle() #turtle.Turtle() means creating an object
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup() #prevents it from making a line to the nearest object, if its equally distanced, there is no line.
ball.goto(0,0)
sleep(1)
ball.dx = 0.175 #the ball will move x pixels to the right
ball.dy = 0.175 # the ball will move y pixels up #0.175

#scoretext blue
st = turtle.Turtle()
st.speed(0)
st.color("blue")
st.penup()#prevents object from making a line
st.hideturtle()
st.goto(0,260)
st.write("TEAM BLUE, 0  ", align="right", font=("Press Start",15,"bold"))

#scoretext red
st.speed(0)
st.color("red")
st.penup()#prevents object from making a line
st.hideturtle()
st.goto(0,260)
st.write("  TEAM RED, 0", align="left", font=("Press Start",15,"bold"))

#scoretext center
st.speed(0)
st.color("black")
st.penup()#prevents object from making a line
st.hideturtle()
st.goto(0,260)
st.write(":", align="center", font=("Press Start",15,"bold"))







#Functions

def pa_up():
    y = pa.ycor()
    y += 20
    pa.sety(y)
def pa_down():
    y = pa.ycor()
    y -= 20
    pa.sety(y)
def pb_up():
    y = pb.ycor()
    y += 20
    pb.sety(y)
def pb_down():
    yb = pb.ycor()
    yb -= 20
    pb.sety(yb)

#Keybinding
window.listen() #listens for key presses (ikr kinda stupid command name)

window.onkeypress(pa_up, "w") #calls function pa_up when "w" is pressed
window.onkeypress(pa_up,'W')
window.onkeypress(pa_down, "s")
window.onkeypress(pa_down, "S")
window.onkeypress(pb_up, "Up")
window.onkeypress(pb_down, "Down")


#main game loop
while True:
    window.update()




    #moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #check borders of window
    if ball.ycor() > 255:
        ball.sety(255)
        ball.dy *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC) #makes it play the pop.mp3 sound, the winsound.SND_ASYNC part makes it so that everything continues while the sound plays.


    if ball.ycor() < -282.5:
        ball.sety(-282.5)
        ball.dy *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)

    if ball.xcor() > 402:
        winsound.PlaySound("cheer.wav", winsound.SND_ASYNC)
        sleep(5)
        st.clear()
        ball.goto(0,0)
        ball.dx *= -1
        sa += 1
        st.clear()
        st.color("blue")
        st.write("TEAM BLUE, {}  ".format(sa), align="right", font=("Press Start", 15, "bold"))
        st.color("red")
        st.write("  TEAM RED, {}".format(sb), align="left", font=("Press Start", 15, "bold"))
        st.color('black')
        st.goto(0, 260)
        st.write(":", align="center", font=("Press Start", 15, "bold"))
    if ball.xcor() < -402:
        winsound.PlaySound("cheer.wav", winsound.SND_ASYNC)
        sleep(5)
        st.clear()
        ball.goto(0,0)
        ball.dx *= -1
        sb += 1
        st.color("red")
        st.write("  TEAM RED, {}".format(sb), align="left", font=("Press Start", 15, "bold"))
        st.color("blue")
        st.write("TEAM BLUE, {}  ".format(sa), align="right", font=("Press Start", 15, "bold"))
        st.color("black")
        st.goto(0, 260)
        st.write(":", align="center", font=("Press Start", 15, "bold"))









    #code ball colliding with paddle
    if (ball.xcor() > 335 and ball.xcor() < 355) and (ball.ycor() < pb.ycor() + 40 and ball.ycor() > pb.ycor() - 40):
        #run if the edges are touching AND is it between the top and bottom of the paddle
        ball.setx(335)
        ball.dx *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -332.5 and ball.xcor() < -335) and (ball.ycor() < pa.ycor() + 40 and ball.ycor() > pa.ycor() - 40):
        #run if the edges are touching AND is it between the top and bottom of the paddle
        ball.setx(-332.5)
        ball.dx *= -1
        winsound.PlaySound("pop.wav", winsound.SND_ASYNC)
