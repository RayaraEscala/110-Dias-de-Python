print('Neste projeto vamos usar o Conversor de real em moedas')
reais = float(input('Quantos reais você tem na carteira: R$ '))
conversor = input('Escolha a moeda a ser convertida (dolar, euro, iene, yuan): ')

match conversor.lower():
    case 'dolar':
        res = reais / 5.5627
    case 'euro':
        res = reais / 6.1704
    case 'iene':
        res = reais / 0.0349
    case 'yuan':
        res = reais / 0.8386
    case _:
        res = None

if res is not None:
    print(f'O valor de R$ {reais} equivale a {res:.2f}')
else:
    print('Moeda inválida.')