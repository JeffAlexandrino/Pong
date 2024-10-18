import turtle
import os

# Propriedades da tela
sc = turtle.Screen()
sc.title("Pypong")  # Nome
sc.bgcolor("black")  # Cor de fundo
sc.setup(width=1000, height=600)  # Proporção

# Propriedades da raquete esquerda
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")  # Formato
left_pad.color("white")  # Cor
left_pad.shapesize(stretch_wid=6, stretch_len=2)  # Tamanhos
left_pad.penup()
left_pad.goto(-400, 0)

# Propriedades da raquete direita
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")  # Formato
right_pad.color("purple")  # Cor
right_pad.shapesize(stretch_wid=6, stretch_len=2)  # Tamanhos
right_pad.penup()
right_pad.goto(400, 0)

# Propriedades da bola
hit_ball = turtle.Turtle()
hit_ball.speed(75)
hit_ball.shape("circle")
hit_ball.color("red")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Pontuação inicial
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

# Funções para movimentar as raquetes
def paddleaup():
    y = left_pad.ycor()
    if y < 250:  # Limite superior
        y += 20
        left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    if y > -250:  # Limite inferior
        y -= 20
        left_pad.sety(y)

def paddlebup():
    y = right_pad.ycor()
    if y < 250:  # Limite superior
        y += 20
        right_pad.sety(y)

def paddlebdown():
    y = right_pad.ycor()
    if y > -250:  # Limite inferior
        y -= 20
        right_pad.sety(y)

# Define os comandos
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "o")
sc.onkeypress(paddlebdown, "k")

# Loop do jogo
while True:
    sc.update()
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Colisão da bola com as bordas superiores e inferiores
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    # Atualiza a pontuação se a bola passar das raquetes
    if hit_ball.xcor() > 480:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        hit_ball.dy *= -1
        Jogador1 += 1
        sketch.clear()
        sketch.write("Jogador1 : {}    Jogador2: {}".format(
            Jogador1, Jogador2), align="center",
            font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -480:
        hit_ball.goto(0, 0)
        hit_ball.dx *= -1
        hit_ball.dy *= -1
        Jogador2 += 1
        sketch.clear()
        sketch.write("Jogador1 : {}    Jogador2: {}".format(
            Jogador1, Jogador2), align="center",
            font=("Courier", 24, "normal"))

    # Colisão da bola com as raquetes
    # Área de colisão para a raquete direita
    if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370 and 
        hit_ball.ycor() < right_pad.ycor() + 60 and 
        hit_ball.ycor() > right_pad.ycor() - 60):
        hit_ball.setx(360)
        hit_ball.dx *= -1
        os.system('aplay bounce.wav&')  # Ajuste o comando para Windows/Mac conforme necessário

    # Área de colisão para a raquete esquerda
    if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370 and 
        hit_ball.ycor() < left_pad.ycor() + 60 and 
        hit_ball.ycor() > left_pad.ycor() - 60):
        hit_ball.setx(-360)
        hit_ball.dx *= -1
        os.system('aplay bounce.wav&')  # Ajuste o comando para Windows/Mac conforme necessário
