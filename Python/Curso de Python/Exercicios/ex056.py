i1 = 0
nf = 'i'
mdi = 0
mv = 0
h = 0
m = 0


for v1 in range(1, 5):
    print(f'----- {v1}ª PESSOA ----')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    s = str(input('SEXO [M/F]: ')).strip().upper()
    mdi = mdi + idade

    if s == 'M':
        if v1 == 1:
            mv = idade
            nf = nome
        else:
            if mv < idade:
                mv = idade
                nf = nome
        h = h + 1
    if s == 'F':
        if idade < 20:
            i1 = i1 + 1
        m = m + 1
print('--------------------')
print('')
print('--------------------'*2)
if h == 0:
    print(f'A MEDIA DE IDADE DO GRUPO E DE {mdi / 4:.1f} ANOS')
    print('NAO HA HOMENS NESTA LISTA')
    print(f'AO TODO SAO {i1} MULHERES COM MENOS DE 20 ANOS')
elif m == 0:
    print(f'A MEDIA DE IDADE DO GRUPO E DE {mdi / 4:.1f} ANOS')
    print(f'O HOMEM MAIS VELHO SE CHAMA {nf} E TEM {mv} ANOS')
    print('NAO HA MULHERES')
else:
    print(f'A MEDIA DE IDADE DO GRUPO E DE {mdi / 4} ANOS')
    print(f'O HOMEM MAIS VELHO SE CHAMA {nf} E TEM {mv} ANOS')
    print(f'AO TODO SAO {i1} MULHERES COM MENOS DE 20 ANOS')

print('--------------------'*2)

