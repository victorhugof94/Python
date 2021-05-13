num = int(input('Digite uma numero:'))
b = bin(num)
o = oct(num)
h = hex(num)
print('''Escolha
[1] binario
[2] octal
[3] hex ''')
opcao = int(input('sua Opcao: '))
if opcao == 1:
    print('{} convertido {}'.format(num,b[2:]))
elif opcao == 2:
    print('{} convertido {}'.format(num,o[2:]))
elif opcao == 3:
    print('{} convertido {}'.format(num,h[2:]))

