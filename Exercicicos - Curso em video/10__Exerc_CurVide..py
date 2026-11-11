print('Neste projeto vamos usar o Conversor de real em moedas')
a = float(input('Quantos reais você tem na carteira: R$ '))
conversor = input('Escolha a moeda a ser convertida (dolar, euro, iene, yuan): ')

match conversor.lower():
    case 'dolar':
        res = a / 5.5627
    case 'euro':
        res = a / 6.1704
    case 'iene':
        res = a / 0.0349
    case 'yuan':
        res = a / 0.8386
    case _:
        res = None

if res is not None:
    print(f'O valor de R$ {a} equivale a {res:.2f}')
else:
    print('Moeda inválida.')