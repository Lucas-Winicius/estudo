valores = list()
for cont in range(0, 5):
    valores.append(int(input('DIGITE UM VALOR: ')))


for c, v in enumerate(valores):
    print(f'NA POSIÇAO {c + 1} ENCONTREI O VALOR {v}')
print('FIM')
