salario = float(input('Qual o seu Salario'))
if salario >= 1250:
    aumento= salario*(1+10/100)
    print('o seu aumento é R${:.2f}'.format(aumento))
else:
    aumento2=salario*(1+15/100)
    print('o seu auemnto é R${:.2f}'.format(aumento2))

