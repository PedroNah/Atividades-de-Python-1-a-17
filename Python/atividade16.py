#16. Receba a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o
#número de descendentes. Calcule o salário que serão as horas trabalhadas x o valor por hora.
#Calcule o salário líquido (= Salário Bruto – desconto). A cada dependente será acrescido R$ 100
#no Salário Líquido. Exiba o salário a receber.
horasW = float(input("Qual é o tempo de horas trabalhadas? "))
ValorH = float(input("Qual é o valor por hora? "))
Desconto = float(input("Qual é o percentual de desconto? "))
Desconto = float(1 - Desconto / 100)
Dependente = int(input("Possui algum dependente/s? "))
SalarioB = float(horasW  * ValorH)
SalarioL = float(SalarioB * Desconto)
Salario = (SalarioL + (Dependente * 100))
print("O salário que receberá é de: ", Salario)