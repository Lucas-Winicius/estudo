v1 = float(input('QUAL A DISTANCIA DA SUA VIAJEM? '))

if v1 <= 200:
    print(f'O VALOR DE SUA PASSAGEM SERA DE R${v1 * 0.50:.2f}')
else:
    print(f'O VALOR FINAL DE SUA PASSAGEM SERA DE R${v1 * 0.45:.2f}')

print('PARA COMPRAR A PASSAGEM ENTRE EM NOSSO SITE')
print('BOA VIAGEM!')
