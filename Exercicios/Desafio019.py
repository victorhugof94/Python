import random
a = input('digite o primero aluno:')
b = input('digite o segundo aluno:')
c = input('digite o terceiro aluno:')
d = input('digite o quarto  aluno:')
Lista = [a,b,c,d]
r = random.choice(Lista)
print(' aluno sorteado {}'.format(r))
