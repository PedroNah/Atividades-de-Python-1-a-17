#5. Receba os coeficientes A, B e C de uma equação do 2o grau (AX2+BX+C=0). Calcule e mostre as raízes reais (considerar que a equação possui 2 raízes reais).
A = float
B = float
C = float
delta = float
x1 = float
x2 = float
A = float(input("Qual o valor de A? (não pode ser 0) "))
B = float(input("Qual o valor de B? "))
C = float(input("Qual o valor de C? "))
delta = ((B**2)-4*A*C)
print("O valor de delta é: ", delta)
x1 = (-B-(delta ** (1/2))) / (2 * A)
print("A raiz negative é: ", x1)
x2 = (-B+(delta ** (1/2))) / (2 * A)
print("A raiz positiva é: ", x2)