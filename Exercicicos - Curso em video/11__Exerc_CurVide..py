print('Neste projeto vamos calcular a quantidade de tinta para uma parede')
largura = float(input('Quantos metros mede o largura da parede?'))
altura = float(input('Quantos metros mede o altura da parede?'))

area = largura * altura
tinta = area / 2

print('Em uma parede de {} m² gastamos {:.1f} l de tinta'.format(area, tinta))