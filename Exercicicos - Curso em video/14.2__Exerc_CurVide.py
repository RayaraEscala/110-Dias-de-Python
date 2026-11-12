print('Vamos converter a temperatura de Celsius para outras escalas')
temp = float(input("Qual a temperatura em Celsius: "))

Conversao = input('Deseja converter para qual temperatura? (Kelvin, Fahrenheit): ')

match Conversao:
    case 'Kelvin':
        resultado = temp + 273.15
        print(f'A temperatura {temp}°C é igual a {resultado:.2f} K')
    case 'Fahrenheit':
        resultado = temp * 9/5 + 32
        print(f'A temperatura {temp}°C é igual a {resultado:.2f}°F')
    case _:
        print('Opção inválida. Digite "Kelvin" ou "Fahrenheit".')