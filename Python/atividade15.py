#15. Receba os valores de 2 catetos de um triângulo retângulo. Calcule e mostre a hipotenusa.
Cat1 = float(input("Qual é o valor do primeiro cateto? "))
Cat2 = float(input("Qual é o valor do segundo cateto? "))
hip = ((Cat1 ** 2) + (Cat2 ** 2)) ** 0.5
hip = round(hip, 2)
print("O valor da hipotenusa é: ", hip)