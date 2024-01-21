#   Código fonte de um jogo Pong utilizando o módulo Turtle
#   Nota: É importante ter uma versão do Python 3.6+ ou a parte do placar pode causar problemas.
#------------------------------------------------------------------------------------------------------
import turtle 

#Propriedades da tela
sc = turtle.Screen()
sc.title("Pypong") #Nome
sc.bgcolor("black") #Cor de fundo
sc.setup(width = 1000, height = 600) #Proporção

#Propriedades da raquete esquerda
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square") #Formato
left_pad.color("white") #Cor
left_pad.shapesize(stretch_wid = 6, stretch_len = 2) #Tamanhos
left_pad.penup()
left_pad.goto(-400, 0)

#Propriedades da raquete direita
left_right = turtle.Turtle()
left_right.speed(0)
left_right.shape("square") #Formato
left_right.color("blue") #Cor
left_right.shapesize(stretch_wid = 6, stretch_len = 2) #Tamanhos
left_right.penup()
left_right.goto(-400, 0)

#Propriedades da bola
hit_ball = turtle.Turtle()
hit_ball.speed(75) 
hit_ball.shape("circle") 
hit_ball.color("red")
hit_ball.goto(0, 0) 
hit_ball.dx = 5  
hit_ball.dy = -5 

#Pontuação inicial
Jogador1 = 0
Jogador2 = 0

sketch = turtle.Turtle() 
sketch.speed(0) 
sketch.color("blue") 
sketch.penup() 
sketch.hideturtle() 
sketch.goto(0, 260) 
sketch.write("Jogador1 : 0    Jogador2: 0", 
             align="center", font=("Courier", 24, "normal")) 

def paddleaup():
    y = left_pad.ycor()
    y += 20
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    y -= 20
    left_pad.sety(y)

def paddlebup():
    y = right_pad.ycor()
    y += 20
    left_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    y -= 20
    left_pad.sety(y)

#Define os comandos 
sc.listen() 
sc.onkeypress(paddleaup, "w") 
sc.onkeypress(paddleadown, "s") 
sc.onkeypress(paddlebup, "o") 
sc.onkeypress(paddlebdown, "k") 

while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor()+hit_ball.dx)
    hit_ball.sety(hit_ball.ycor()+hit_ball.dy)

    if hit_bally() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_bally() > 280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    if hit_ball.xcor() > 500: 
        hit_ball.goto(0, 0) 
        hit_ball.dy *= -1
        Jogador1 += 1
        sketch.clear() 
        sketch.write("Jogador1 : {}    Jogador2: {}".format( 
                      Jogador1, Jogador2), align="center", 
                      font=("Courier", 24, "normal"))

    if hit_ball.xcor() > -500: 
        hit_ball.goto(0, 0) 
        hit_ball.dy *= -1
        Jogador2 += 1
        sketch.clear() 
        sketch.write("Jogador1 : {}    Jogador2: {}".format( 
                      Jogador1, Jogador2), align="center", 
                      font=("Courier", 24, "normal")) 

    
