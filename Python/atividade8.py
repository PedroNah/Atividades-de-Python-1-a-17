#8. Receba o valor de um depósito em poupança. Calcule e mostre o valor após 1 mês de aplicação sabendo que rende 1,3% a. m.
deposito = float(input("Qual o valor do depósito? "))
deposito = (deposito * 1.013)
deposito = round(deposito, 2) #pesquisado na internet por causa do problema de erro de ponto flutuante
print("Após um mês, esse é o valor: R$", deposito)