vel = int(input('Qual a velocidade atual do carro '))
if vel >80:
    multa = (vel-80)* 7.00
    print('Multado e sua multa é de R${:.2f}'.format(multa))
print('tenha um bom dia ')