import turtle

wn = turtle.Screen()
wn.title("Ping pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0


# Raquette 1
raquette_1 = turtle.Turtle()
raquette_1.speed(0)
raquette_1.shape("square")
raquette_1.color("white")
raquette_1.shapesize(stretch_wid=5, stretch_len=1)
raquette_1.penup()
raquette_1.goto(-350, 0)


# Raquette 2
raquette_2 = turtle.Turtle()
raquette_2.speed(0)
raquette_2.shape("square")
raquette_2.color("white")
raquette_2.shapesize(stretch_wid=5, stretch_len=1)
raquette_2.penup()
raquette_2.goto(350, 0)


# Balle
balle = turtle.Turtle()
balle.speed(0)
balle.shape("square")
balle.color("green")
balle.penup()
balle.goto(0, 0)
balle.dx = 0.70
balle.dy = 0.70

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Joueur 1: {}  Joueur 2: {}".format(score_1, score_2), align=("center"), font=("Courier", 24, "normal"))


# Les fonctions pour la raquette_1
def raquette_1_up():
    y = raquette_1.ycor()
    y += 20
    raquette_1.sety(y)
    

def raquette_1_down():
    y = raquette_1.ycor()
    y -= 20
    raquette_1.sety(y)


# Les fonctions pour la raquette_2
def raquette_2_up():
    y = raquette_2.ycor()
    y += 20
    raquette_2.sety(y)


def raquette_2_down():
    y = raquette_2.ycor()
    y -= 20
    raquette_2.sety(y)  

# Keyboard Binding
wn.listen()

# Raquette_1 mouvement Haut et Bas
wn.onkeypress(raquette_1_up, "w")
wn.onkeypress(raquette_1_down, "s")

# Raquette_2 mouvement Haut et Bas
wn.onkeypress(raquette_2_up, "Up")
wn.onkeypress(raquette_2_down, "Down")


# Boucle principale infini du jeu 
while True:
    wn.update()


    # Mouvement de la balle

    balle.setx(balle.xcor() + balle.dx)
    balle.sety(balle.ycor() + balle.dy)

    # Border checking 

        # Bare du haut (rebond)

    if balle.ycor() > 290:
        balle.sety(290)
        balle.dy *= -1

        # Bare du bas (rebond)

    if balle.ycor() < -290:
        balle.sety(-290)
        balle.dy *= -1

        # Bare de droite (gain de point + reset de position en (0, 0))

    if balle.xcor() > 390:
        balle.goto(0, 0)
        balle.dx *= -1  
        score_1 += 1
        pen.clear()
        pen.write("Joueur 1: {}  Joueur 2: {}".format(score_1, score_2), align=("center"), font=("Courier", 24, "normal"))  
        

        # Bare de gauche (gain de poin + reset de position en (0, 0))

    if balle.xcor() < -390:
        balle.goto(0, 0)
        balle.dx *= -1
        score_2 += 1
        pen.clear()
        pen.write("Joueur 1: {}  Joueur 2: {}".format(score_1, score_2), align=("center"), font=("Courier", 24, "normal"))  
       

    # Collision entre la balle et la raquette_2

    if (balle.xcor() > 340 and balle.xcor() < 350) and (balle.ycor() < raquette_2.ycor() + 40 and balle.ycor() > raquette_2.ycor() -40):
        balle.setx(340)
        balle.dx *= -1

      # Collision entre la balle et la raquette_1

    if (balle.xcor() < -340 and balle.xcor() > -350) and (balle.ycor() < raquette_1.ycor() + 40 and balle.ycor() > raquette_1.ycor() -40):
        balle.setx(-340)
        balle.dx *= -1 
   
      # Collision entre bordure haut et raquette_2
    if raquette_2.ycor() > 255 :
        raquette_2.sety(max(0, 255))

      # Collision entre bordure bas et raquette_2
    if raquette_2.ycor() < -255 :
        raquette_2.sety(min(0, -255))    

      # Collision entre bordure haut et raquette_1
    if raquette_1.ycor() > 255 :
        raquette_1.sety(max(0, 255))

      # Collision entre bordure bas et raquette_1
    if raquette_1.ycor() < -255 :
        raquette_1.sety(min(0, -255))           






