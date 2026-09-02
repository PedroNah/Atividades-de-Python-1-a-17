#14. Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3o ângulo.
angulo1 = float(input("Digite o primeiro ângulo: "))
angulo2 = float(input("Digite o segundo ângulo: "))
angulo3 = 180 - (angulo1 + angulo2)
print("O valor do 3º ângulo é: ", angulo3)