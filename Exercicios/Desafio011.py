lar = float(input('largura da parede:'))
alt = float(input('altura da parede:'))
area= lar * alt
lt = area/2
print ( 'sua parede é de {:.2f}m x {:.2f}m \n com uma area de {}m2\n sendo assim sera necessario {}l de tinta para a pintura'.format(lar, alt,area,lt))