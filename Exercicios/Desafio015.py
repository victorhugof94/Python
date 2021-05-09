km = float(input('quantos Km rodas:'))
dias = int(input('quantos dias utlizados:'))
valor = (60*dias)+(km*0.15)
print('o valor do aluguel é R${:.2f}'.format(valor))
