print('Neste projeto vamos enviar o antecessor e o sucessor do numero digitado')
num = int(input('Qual o seu numero?'))
#-ant = num - 1 -suc = num + 1 - Poderiam ser as variáveis ant e suc ou direto no print?
# Se fosse usar no programa os números antecessor e sucessor, aí seria necessário ter esta variável separada.
print('O número {} tem seu antecessor o {} e o sucessor é {}.'.format(num, (num-1), (num+1)))