print('Neste projeto vamos calcular o valor de um aluguel de carros')
dias = int(input('Quantos dias foi alugado?'))
km = float(input('Qual a quantidade de km rodados?'))

valor = dias * 60 + km * 0.15

print('O valor do aluguel do carro por {} dias e {:.2f} km rodados equivale a {:.2f}'.format(dias,km,valor))