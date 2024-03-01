# Snake Game Project by Nikul 

import turtle 
import time
import random

# The above three modules are required to create the Snake game. 
# Turtle is used to create different graphics and shapes. 
# Time is used to create time related functions such as sleep. Random is used to generate random numbers


delay = 0.1 
score = 0
high_score = 0

# The above code is used to set up the inital variables for the Snake game. Delay is used to create a time delay for the snakes movement.
# The score is used to monitor a players progress through the gameplay.
# High score is the highest score a player will have obtained overall.

window = turtle.Screen()
window.title("Snake Game by Nikul")
window.bgcolor("yellow")
window.setup(width=600, height=600)
window.tracer(0)

# The above block of code is used to create a seperate window from which the game is played.

head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.penup()
head.goto(0,0)
head.direction = "stop"

# The above block of code is used to create the snakes head and define its various properties.

food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("green")
food.penup()
food.goto(0,100)

# The above block of code is used to define the food that the snake will consume in order to get larger during the gameplay.

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Segments is used to store the snakes body parts and pen is used to create the scoreboard for the Snake Game in the above block of code.

def go_up():
    if head.direction != "down":  
        head.direction = "up"
    
def go_down():
    if head.direction != "up":  
        head.direction = "down"
    
def go_left():
    if head.direction != "right":  
        head.direction = "left"
    
def go_right():
    if head.direction != "left":  
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
        
    if head.direction == "left":
        x = head.xcor()  
        head.setx(x - 20)  
    
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# This block of code above defines how the snake head will move in all directions during the gameplay.


window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")  
window.onkeypress(go_left, "a")  
window.onkeypress(go_right, "d")  

# This block of code assigns specific keys on the keyboard for the directions that the snake will travel in during gameplay.


while True: 
    window.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:  
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        for segment in segments:
            segment.goto(1000, 1000)

        segments.clear()
        score = 0
        pen.clear()    
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()    
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()  
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segments:
                segment.goto(1000, 1000)

            segments.clear()

    time.sleep(delay)

window.mainloop()

#The next large chunk of code is the main game loop. This controls the flow of the game and defines the main outcome of the game. The code checks for collisions with the wall, food and the snakes own body ensuring that the gameplay is stopped where necessary and the correct points are calculated and allocated accordingly to the player.
# window.mainloop() code keeps the game window open on the screen until the player chooses to close the window manually.add()
# This concludes my project on the Python Snake game. 