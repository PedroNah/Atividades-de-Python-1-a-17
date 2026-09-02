#7. Receba os valores do comprimento, largura e altura de um paralelepípedo. Calcule e mostre seu volume.
comprimento = float
largura = float
altura = float
volume = float
comprimento = float(input("Qual é o comprimento? "))
largura = float(input("Qual é o largura? "))
altura = float(input("Qual é o altura? "))
volume = (comprimento*largura*altura)
print("O volume do paralelepípedo é: ", volume)