import turtle
import time
import random

delay = 0.1

#Score
score = 0
high_score = 0

#Screen details
scrn = turtle.Screen()
scrn.title("Welcome to the Romeo Snake Game!!!")
scrn.bgcolor("red")
scrn.setup(width=600, height=600)
scrn.tracer(0)

#head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"

#Da food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("white")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))

#moving functions
def go_up():
    if head.direction != "down":
        head.direction ="up"

def go_down():
    if head.direction != "up":
        head.direction ="down"

def go_right():
    if head.direction != "left":
        head.direction ="right"

def go_left():
    if head.direction != "right":
        head.direction ="left"    




def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)


# key movment
scrn.listen()
scrn.onkeypress(go_up, "w")
scrn.onkeypress(go_down, "s")
scrn.onkeypress(go_left, "a")
scrn.onkeypress(go_right, "d")

#game loop
while True:
    scrn.update()

    #Borders
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear segment list
        segments.clear()


        #reset score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))




    if head.distance(food) < 20:
        # Move the food after it gest eaten
        x = random.randint(-290, 290)
        y = random.randint(-290, 260)
        food.goto(x,y)
        
        #add segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        #increaze score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    # Feed the snake
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to the head
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()

    # check for head collion with self
    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            #hide segments
            for segment in segments:
                segment.goto(1000, 1000)

            #clear segments
            segments.clear()

            score = 0
            #reset score

        
            pen.clear()
            pen.write("Score: {} High Score {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))


    time.sleep(delay)


scrn.mainloop()
