dist = int(input('Distancia da sua viagem:'))
if dist <= 200:
    v200 = dist*0.50
    print (' Valor da sua viagem é R${:.2f}'.format(v200))
else:
    vd = dist * 0.45
    print('Valor da sua viagem é R${:.2f}'.format(vd))
