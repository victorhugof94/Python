import datetime
atual = datetime.date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print(' Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('voce tem que se alistar imdiatamente')
elif idade <18 :
    saldo = 18-idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print(' aliste-se em {}'.format(ano))
elif idade > 18 :
    saldo = idade - 18 
    print(' voce ja deveria ter se alistado ha {} anos'.format(saldo))
    ano = atual - saldo
    print (' seu alistamento foi em {}'.format(ano))