#17. Calcule a quantidade de litros gastos em uma viagem, sabendo que o automóvel faz 12 km/l.
#Receber o tempo de percurso e a velocidade média.
TempoP = float(input("Qual é o tempo do percuso em horas? "))
VelocidadeM = float(input("Qual é a velocidade média em km/h? "))
Distancia = (TempoP * VelocidadeM)
LitrosG = (Distancia / 12)
print("A quantidade de litros gastos é: ",  LitrosG)