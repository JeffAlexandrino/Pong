import turtle 

sc = turtle.Screen()
sc.title("Jogo Pong")
sc.bgcolor("black")
sc.setup(width = 1000, height = 600)

#Propriedades da raquete esquerda
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")#Formato
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
