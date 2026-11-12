print('Neste projeto vamos calcular o Descontos')
preco = float(input('Quanto custa o produto? R$ '))
desc = preco - (p1 * 0.05)
print('O produto que vale {} com 5% de desconto ficar R$ {:.2f}'.format(preco, desc))
