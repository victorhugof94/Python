vc = float(input('Qual o valor da casa: R$'))
s = float(input('Qual o seu salario'))
a = int(input('Em quantos anos voce quer pagar :'))
m = a * 12
p = vc/m

if s*(30/100) >= p :
    print ('O emprestimo sera feito em {} anos com prestacoes mensais de R${:.2f} e foi aprovado '.format(a,p))
else:
    print(' Emprestimo nao aprovado a prestacao de R${:.2f} e passa dos 30% so seu salario'.format(p))
