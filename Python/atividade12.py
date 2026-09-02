#12. Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e quantos anos terá daqui a 17 anos.
AnoNascimento = int(input("Que ano você nasceu? "))
AnoAtual = int(input("Qual é o ano atual? "))
idade = int(AnoAtual - AnoNascimento)
idade17 = int(idade + 17)
print("Sua idade é: ", idade, "Sua idade daqui 17 anos será: ", idade17)