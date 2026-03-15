'''
Description: In this Python Turtle Graphics-based game, you are tasked with shooting down a Tie Fighter from the Star Wars universe, which will be maneuvering randomly against a vibrant backdrop of stars and planets. Control an aiming reticle with the arrow keys to target and shoot the Tie Fighter using the space-bar. The game tracks your hits, and achieving three successful strikes on the Tie Fighter will prompt a game over screen, asking if you wish to play again.

Game Mechanics:

Tie Fighter: The Tie Fighter will be a graphical object that randomly moves across a celestial canvas filled with stars and the occasional passing planet. Use Turtle Graphics to draw and animate the Tie Fighter, ensuring it remains within the visible galaxy (screen boundaries).
Background: Use Turtle graphics to draw stars and planets in the background (5 stars, 1 planet) based on your previous assignment. 
Reticle: The reticle, designed as a circle with crosshairs, is controlled using the arrow keys (up, down, left, right) for aiming.
Shooting: Pressing the space-bar fires a red laser from the reticle's position. Implement this using four lines that converge on the reticle's center to simulate the laser blast.
Hit Detection: Calculate if a laser hit is successful by checking if the center of the reticle aligns with the center of the Tie Fighter using the formula D=(xf??xr?)**2+(yf??yr?)**2?.
Scoring: Track the number of times the Tie Fighter is hit. Three successful hits conclude the gameplay, displaying "Game Over" prominently against the starry background.
Game Over: The game prompts the player if they want to replay upon achieving three hits or by pressing the escape key.
Additional Tips:

Base your game mechanics on the provided square animation tutorial, incorporating onkeypress and onkeyrelease functions from the Turtle module.
Maintain global coordinates for both the Tie Fighter and the reticle (xf, yf, xr, yr).
Use the random library for the Tie Fighter's unpredictable movements.
Draw the background, then the fighter, then the reticle, and lastly, the lasers.
Organize your code using functions or classes to enhance modularity and maintainability.
This immersive space battle experience not only tests your aiming skills but also places you right in the middle of an interstellar conflict against the backdrop of a dynamically rendered universe.
'''

import turtle as t
import random as r
import math as m

t.tracer(0,0)

# Global Variables
screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("purple")

# Background - Stars and Planet
# Draw stars function as small orange dots
def Draw_Stars(x, y):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.dot(6, "orange")

# Draw planets function as big grey dots
def Draw_Planets(x, y):
    t.hideturtle()
    t.penup()
    t.goto(x, y)
    t.dot(50, "grey")
    
# Planets and Stars background function being defined
def background_StarsandPlanets():
    Stars= [(r.randint(-screen.window_width()//2, screen.window_width()//2), r.randint(-screen.window_width()//2, screen.window_width()//2)) for i in range(6)]#Array that Uses my specified offscreen bounds to draw 6 orange stars in the specifdied bounds in random positions, using the random library 
    Planets= [(r.randint(-screen.window_height()//2, screen.window_height()//2), r.randint(-screen.window_height()//2, screen.window_height()//2)) for i in range(1)]#Array that Uses my specified offscreen bounds to draw 1 grey planets in the specifdied bounds in random positions, using the random library
#Drawing the orange stars and grey planets for loop to draw planets and Stars
    for star_x,star_y in Stars:
        Draw_Stars(star_x,star_y)
        
    for planet_x,planet_y in Planets:
        Draw_Planets(planet_x,planet_y)
        
background_StarsandPlanets()
#--------------------------------------------------------------------
#Tie Fighter being drawn
class TieFighter:
    def __init__(self):
        self.x=r.randint(-300,300)
        self.y=r.randint(-200,200)#attributes, I couldnt get this program to ework with xf,xr,yf,yr, so I made just an x and y term and randomly made cords, so that the tie fighter could move.
        self.speed=2
        self.heading=r.randint(0,360)

    def draw(self): #draw my tie fighter, I tried my best to get this drawn correctly, at least for a 2D model. I made a circle with the 2 wings.
        t.penup()
        t.goto(self.x,self.y)
        t.setheading(self.heading)
        t.color("black")
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.pendown()
        t.left(90)
        t.forward(30)
        t.forward(60)
        t.left(90)
        t.forward(30)
        t.right(180)#turtle commands to draw tiefighter anmd make its color black like in movies with goto and set heading functions.
        t.forward(60)
        t.right(180)
        t.forward(30)
        t.left(90)
        t.forward(100)
        t.forward(50)
        t.left(90)
        t.forward(30)
        t.right(180)
        t.forward(60)
        t.right(180)
        t.forward(30)
        t.left(90)
        t.penup()
    def move(self):
        self.x += self.speed * m.cos(m.radians(self.heading))
        self.y += self.speed * m.sin(m.radians(self.heading))
        if self.x < -screen.window_width()/2 or self.x > screen.window_width()/2:#used math library to use my trig functions so the tiefighter could move at angles(I also used the formula you gave me just expoanded on it a little)
            self.heading = 180 - self.heading
        if self.y < -screen.window_height()/2 or self.y > screen.window_height()/2:
            self.heading = -self.heading
#----------------------------------------------------
#Reticle/crosshair class
class Reticle:
    def __init__(self):
        self.x=0
        self.y=0#attributes

    def draw(self):
        t.penup()
        t.goto(self.x,self.y-10)
        t.setheading(90)
        t.color("red")
        t.pendown()
        t.begin_fill()
        t.end_fill()
        t.penup()
        t.goto(self.x, self.y)#draw the reticle, I made it a red cross
        t.setheading(0)
        t.pendown()
        t.forward(10)
        t.backward(20)
        t.forward(10)
        t.setheading(90)
        t.forward(10)
        t.backward(20)
        t.forward(10)

    def move_up(self):
        self.y+=10

    def move_down(self):
        self.y-=10

    def move_left(self): #My up,down,left,right movement for reticle/crosshair
        self.x-=10

    def move_right(self):
        self.x+=10

#Laser classs
class Laser:
    def __init__(self,x,y):
        self.x=x
        self.y=y #attributes
        self.active=False

    def draw(self,reticle_x,reticle_y):
        self.x=reticle_x
        self.y=reticle_y
        t.penup()
        t.goto(self.x,self.y)
        t.color("red")
        if self.active:
            self.draw_corners()
    def check_collision(self,tie_fighter):
        if self.active:
            distance=m.sqrt((self.x-tie_fighter.x)**2+(self.y-tie_fighter.y)**2)#check collision if hit tiefighter
            if distance<20:#hitbox in pixels
                return True
        return False
    def draw_corners(self):#draw laser from 4 corners to center
        if self.active:
            t.penup()
            t.color("red")#red laser
            t.goto(self.x,self.y)#goes to specified cords
            t.pendown()
            angles=[45,135,225,315]
            for angle in angles:  #draw laser beams at 45-degree intervals from 4 corners
                t.setheading(angle)  #set the heading to the current angle
                t.forward(600)  #draw the laser beam
                t.penup()
                t.goto(self.x, self.y)  #move back to the starting position
                t.pendown()  # Put the pen down
#Game class, I have all of my call functions in here and the whole reason game works, I also have my exit screen for when player wins.
class Game:
    def __init__(self):
        self.tie_fighter=TieFighter()
        self.reticle=Reticle()
        self.laser=Laser(0,0)#attributes
        self.score=0
    def play(self):
        t.clear()
        t.hideturtle()
        t.speed(0)
        t.listen()
        screen.listen()
        t.onkeypress(self.reticle.move_up,"Up")
        t.onkeypress(self.reticle.move_down,"Down")
        t.onkeypress(self.reticle.move_left,"Left")
        t.onkeypress(self.reticle.move_right,"Right")#all of my keypresses in gameclass
        t.onkeypress(self.shoot_laser,"space")
        t.onkey(self.release_laser,"space")
        t.onkey(self.quit_game,"Escape")
        background_StarsandPlanets()
        self.update_score()
        while self.score<3:
            self.move_objects()
            self.check_collisions()#checks collisons if over or equal 3, if thats the case, end game
            t.update()
        self.game_over()
    def move_objects(self):
        self.tie_fighter.move()#tie fighter randomly moving so iuts hard to hit
        self.draw_objects()
    def draw_objects(self):
        t.clear()
        background_StarsandPlanets()
        self.tie_fighter.draw()
        self.reticle.draw()
        self.update_score()#objects that are being drawn, I tried putting my draw planets and stars backgorund function out of this so that the background could be static, but I couldnt get the stars or planets to show up. So I just left it in this draw objects method
        self.laser.draw_corners()#draw laser from 4 corners
        self.laser.draw(self.reticle.x,self.reticle.y)#draw laser where crosshair is
    def check_collisions(self):
        if self.laser.check_collision(self.tie_fighter):#see if tie fighter is hit, if it is add a plus 1 ot score, if not. Add nothing
            self.score+=1
            self.release_laser() #Laser will reset after hitting target so it doesnt continue
            self.tie_fighter=TieFighter()
        if self.score>=3:#if game is over or equal to 3 game ends with ending screen 
            self.game_over()
    def update_score(self):
        t.color("white")
        t.penup()
        t.goto(-screen.window_width()//2+10,screen.window_height()//2-30)#updaste score method, this was hard to do in my opinion.
        t.write(f"Score:{self.score}/3",align="left",)#prints "score 0/3, score 1/3.. etc at nthe top left side of window 
        t.update()
    def shoot_laser(self):
        if not self.laser.active:
            self.laser.active=True
            self.laser.x=self.reticle.x#laser being shot=activate, laser not being shot=false which is code below this.
            self.laser.y=self.reticle.y
    def release_laser(self):
        self.laser.active=False
    def quit_game(self):
        screen.bye() #quit game 
    def game_over(self):
        t.clear()
        t.color("black")
        t.goto(0, 0)
        t.write("Game Over",align="center")
        t.goto(0, -50)
        t.write("Press Escape to Quit",align="center")#game over scren using black text in the centerr of the screen.
        t.listen()
        t.onkey(self.quit_game,"Escape")#you can press escape to end program.
        t.done()

t.update()

if __name__=="__main__":#ensure code inside of this runs only when script is executed directly, amkes the game actually work using game=Game() and game.play()
    game=Game()
    game.play()