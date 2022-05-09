print('='*30)
print('     10 TERMOS DE UMA PA')
print('='*30)

v1 = int(input('PRIMEIRO TERMO: '))
v2 = int(input('RAZAO: '))
v3 = v1 + (10 - 1) * v2

for v3 in range(v1, v3 + v2, v2):
    print(f'{v3}', end=' → ')
print('ACABOU')