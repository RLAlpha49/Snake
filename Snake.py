import turtle
import time
import random
 
delay = 0.1
score = 0
high_score = 0
segments = []
 
 
# Creating Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)
 
# Snake Head Turtle
head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
 
# Food/Points
food = turtle.Turtle()
colors = random.choice(['red', 'green'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
 
# Display Score
scoreTurtle = turtle.Turtle()
scoreTurtle.speed(0)
scoreTurtle.shape("square")
scoreTurtle.color("white")
scoreTurtle.penup()
scoreTurtle.hideturtle()
scoreTurtle.goto(0, 250)
scoreTurtle.write("Score : 0  High Score : 0", align="center",
          font=("Ariel", 24, "bold"))
 
# Direction Functions
def group():
    if head.direction != "down":
        head.direction = "up"
 
def godown():
    if head.direction != "up":
        head.direction = "down"
 
def goleft():
    if head.direction != "right":
        head.direction = "left"
 
def goright():
    if head.direction != "left":
        head.direction = "right"
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)

# User Input       
wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")
 
# Game
while True:
    wn.update()
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])

        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()

        score = 0
        delay = 0.1
        scoreTurtle.clear()
        scoreTurtle.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Ariel", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
 
        # Adds Snake Body/Segment
        newSegment = turtle.Turtle()
        newSegment.speed(0)
        newSegment.shape("square")
        newSegment.color("orange")  # tail colour
        newSegment.penup()
        segments.append(newSegment)
        delay -= 0.001
        score += 1

        if score > high_score:
            high_score = score

        scoreTurtle.clear()
        scoreTurtle.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Ariel", 24, "bold"))

    # Segment Movement
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check Collisions
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
 
            score = 0
            delay = 0.1
            scoreTurtle.clear()
            scoreTurtle.write("Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("Ariel", 24, "bold"))
    time.sleep(delay)

wn.mainloop()