c = 0

print('-='*20)
print(' '*11, 'GERADOR DE P.A')
print('-='*20)
print('')

pr = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO: '))
print('')
v3 = pr + (10 - 1) * r
t = 1

while t != 0:
    while pr <= v3:
        print(pr, end=' → ')
        pr = pr + r
        c = c + 1
    print('PAUSA')
    t = int(input('QUANTOS TERMOS VOCE QUER MOSTRAR MAIS? '))
    v3 = pr + (t - 1) * r
print(f'PROGRESSAO FINALIZADA COM {c} TERMOS MOSTRADOS')