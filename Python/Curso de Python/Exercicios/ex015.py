print('-'*20)
print('  LOCADORA ABOBORA')
print('-'*20)
print('')

d = int(input('QUANTOS DIAS ALUGADOS? '))
km = float(input('QUANTOS KM RODADOS? '))

print('')
print('PREÇO POR DIA R$60')
print('PRECO POR KM R$0.15')
print('')

#print(f'O PREÇO TOTAL A PAGAR E DE {d*8+km*0.15}')

v1 = d*60
v2 = km*0.15

print(f'O TOTAL A SE PAGAR E DE R${v1+v2:.2f}')
