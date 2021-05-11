import random
a = input('digite o primero aluno:')
b = input('digite o segundo aluno:')
c = input('digite o terceiro aluno:')
d = input('digite o quarto  aluno:')
lista = [a,b,c,d]
random.shuffle(lista)
print ('nova ordem\n {}'.format(lista))
