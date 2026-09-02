#6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus conteúdos.
x = int
y = int
troca = int
x = int(input("Qual o valor de x? "))
y = int(input("Qual o valor de y? "))
troca = y
y = x
x = troca
print("Valor de x: ", x)
print("Valor de y: ", y)