print('-='*20)
print('        10 TERMOS DE UM  P.A')
print('-='*20)
print('')

pr = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
print('')
v3 = pr + (10 - 1) * r

while pr <= v3:
    print(pr, end=' → ')
    pr = pr + r
print('FIM')