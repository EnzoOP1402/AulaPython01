valor = float(input('Digite o valor da compra: '))
taxa = float(input('Digite a taxa da prestação: '))
tempo = int(input('Digite o tempo de atraso da prestação: '))
prest = valor + (valor * (taxa/100) * tempo )
print(f'O valor total da prestação com atraso é de {prest}')