#13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
Quilos = float(input("Qual é a quantidade de alimento em quilos? "))
Gramas = float(Quilos * 1000)
dias = int(Gramas / 50)
dias = round(dias, 0)
print("O alimento durará: ", dias)