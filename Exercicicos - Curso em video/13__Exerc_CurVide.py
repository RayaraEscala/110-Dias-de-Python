print('Neste projeto vamos calcular o reajuste salarial')

salario = float(input('Qual o seu salário? R$ '))
reajuste = salario + (salario * 0.15)

print('O seu salário com o reajuste ficará no valor R$ {:.2f} '.format(reajuste))