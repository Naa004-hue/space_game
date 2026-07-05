import turtle 
import math
import random

# screen 
wn = turtle.Screen()
wn.bgcolor('darkblue')
wn.title('random game')
wn.setup(width=630, height=630)
wn.bgpic(("C:/Users/MODT/py/game_2/backg.gif"))
wn.register_shape("C:/Users/MODT/py/game_2/ship.gif")
wn.register_shape("C:/Users/MODT/py/game_2/bomb.gif")
wn.register_shape("C:/Users/MODT/py/game_2/goal.gif")

#borders
class Border(turtle.Turtle) :
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.hideturtle()
        self.penup()
        self.color('white')
        self.setposition(-300,-300)
        self.pendown()
        self.pensize(5)

    def draw(self) :
        wn.tracer(0)
        for side in range(4):
            self.forward(600)
            self.left(90)
            self.hideturtle()
        wn.tracer(1)
#writing score
score=0
score_d = turtle.Turtle()
score_d.color("lavender")
score_d.hideturtle()
score_d.penup()
score_d.goto(-250, 250)   

#writing lives
lives=6
lives_d = turtle.Turtle()
lives_d.color("lavender")
lives_d.hideturtle()
lives_d.penup()
lives_d.goto(-170, 250)   

border=Border()
border.draw()
wn.tracer(0)

#player
class Player(turtle.Turtle) :
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.shape("C:/Users/MODT/py/game_2/ship.gif")
        self.setheading(90)
        self.shapesize(0.75)
        self.m_speed = 5

    def move(self):
        self.fd(self.m_speed)
        if self.xcor()<-290 or self.xcor()> 290 :
            self.left(60)
        if self.ycor()<-290 or self.ycor()> 290 :
            self.left(60)
    
    def turnright(self):
        self.setheading(0)

    def turnleft(self):
        self.setheading(180)

    def speed_up(self):  
        self.m_speed += 0.75

    def goup(self):
        self.setheading(90)

    def godown(self):
        self.setheading(270) 

#goals
class Goals (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("C:/Users/MODT/py/game_2/goal.gif")
        self.shapesize(0.0125)
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
        self.m_speed = 4   
    def moving(self):
        self.fd(self.m_speed)
        if self.xcor()<-270 or self.xcor()> 270 :
            self.left(60)
        if self.ycor()<-270 or self.ycor()> 270 :
            self.left(60) 
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))


#bomb
class Bombs (turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.shape("C:/Users/MODT/py/game_2/bomb.gif")
        self.shapesize(0.0125)
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
        self.m_speed = 4  
    def moving(self):
        self.fd(self.m_speed)
        if self.xcor()<-270 or self.xcor()> 270 :
            self.left(60)
        if self.ycor()<-270 or self.ycor()> 270 :
            self.left(60) 
    def jump(self):
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))

#functions
def isCollision(t1,t2,thr):
    d=math.sqrt(((t1.xcor()-t2.xcor())**2)+((t1.ycor()-t2.ycor())**2))
    if d < thr :
        return True
    else:
        return False

def flash_hit():
    wn.bgcolor('red')
    wn.ontimer(lambda: wn.bgcolor('darkblue'), 100)


player=Player()

#keyboard binding
turtle.listen()
turtle.onkey(player.turnright,'Right')
turtle.onkey(player.turnleft,'Left')
turtle.onkey(player.goup,'Up')
turtle.onkey(player.godown,'Down')

#multiple
goalss=[]
for i in range(8):
    goalss.append(Goals())

bombss=[]
for i in range(8):
    bombss.append(Bombs())

#game over
lost = turtle.Turtle()
lost.color("lavender")
lost.hideturtle()
lost.penup()
lost.goto(-100, 260)   

replay = turtle.Turtle()
replay.color("lavender")
replay.hideturtle()
replay.penup()
replay.goto(-250, 100)   

leave = turtle.Turtle()
leave.color("lavender")
leave.hideturtle()
leave.penup()
leave.goto(20, 100)   

def close_game():
    wn.bye()

hello = turtle.Turtle()
hello.color("cyan")
hello.hideturtle()
hello.penup()
hello.goto(-80, 250)

rules = turtle.Turtle()
rules.color("cyan")
rules.hideturtle()
rules.penup()
rules.goto(-100, 100)

def first_page():
    global hello,rules
    hello.write(f'HELLO !', align="center", font=("Arial", 16, "normal"))

    rules.write(f'-collet the gold coins +10 coins + speed \n -avoid the meteors -1 lives -5 coins \n -press enter to begin ', align="center", font=("Arial", 16, "normal"))
    turtle.onkey(lambda: main_game(reset=False),'Return')

def reseting():
    global lives,score,bombss,goalss
    for goal in goalss :
        goal.moving()
        goal.jump()
        goal.showturtle()
    for bomb in bombss:
        bomb.moving()
        bomb.jump()
        bomb.showturtle()
    player.showturtle()
    player.goto(0, 0)
    player.setheading(90)
    leave.clear()
    replay.clear()
    lost.clear()
    lives = 6
    score = 0
    player.m_speed = 4
    score_d.clear()
    score_d.write(f'Score:{score}', align="center", font=("Arial", 16, "normal"))
    lives_d.clear()
    lives_d.write(f'lives:{lives}', align="center", font=("Arial", 16, "normal"))
    border.draw() 
    wn.tracer(0)

def game_over():
    global lost,replay,leave,lives,score,bombss,goalss
    for seg in bombss:
        seg.hideturtle()
    for seg in goalss:
        seg.hideturtle()
    leave.clear()
    replay.clear()
    lost.clear()
    player.hideturtle()
    score_d.clear()
    lives_d.clear()
    lost.write(f'GAME OVER !', align="left", font=("Arial", 24, "normal"))
   
    replay.write(f'-To restart:\n press Enter ', align="left", font=("Arial", 20, "normal"))
  
    leave.write('-To exit: .\n press space ', align="left", font=("Arial", 20, "normal"))

    turtle.listen()
    turtle.onkey(lambda:main_game(reset=True),'Return')
    turtle.onkey(close_game,'space')

def main_game(reset):
    global lives,score,bombss,goalss,rules,hello
    if reset :
        reseting()
    else :
        hello.clear()
        rules.clear()
        score_d.write(f'Score:{score}', align="center", font=("Arial", 16, "normal"))
        lives_d.write(f'lives:{lives}', align="center", font=("Arial", 16, "normal"))
        player.move()

        for goal in goalss :
            goal.moving()
            if  isCollision(player,goal,20):
                score += 10
                player.speed_up()
                score_d.clear()
                score_d.write(f'Score:{score}', align="center", font=("Arial", 16, "normal"))
                goal.jump()
        for bomb in bombss:
            bomb.moving()
            if  isCollision(player,bomb,20):
                lives -= 1
                score -= 5
                lives_d.clear()
                lives_d.write(f'lives:{lives}', align="center", font=("Arial", 16, "normal"))
                player.goto(0,0)
                bomb.jump()
                flash_hit()
        if lives <= 0 :
            game_over()
            return

    wn.update()
    wn.ontimer(lambda: main_game(False), 50)

first_page()

wn.mainloop()