v1 = int(input('DIGITE O PRIMEIRO  VALOR: '))
v2 = int(input('DIGITE O SEGUNDO VALOR: '))
v3 = int(input('DIGITE O TERCEIRO VALOR: '))

if v1 < v2 and v1 < v3:
    print(f'O MENOR VALOR DIGITADO FOI: {v1}')
if v2 < v1 and v2 < v3:
    print(f'O MENOR VALOR DIGITADO FOI: {v2}')
if v3 < v1 and v3 < v2:
    print(f'O MENOR VALOR DIGITADO FOI {v3}')
if v1 > v2 and v1 > v3:
    print(f'O MAIOR VALOR DIGITADO FOI: {v1}')
if v2 > v1 and v2 > v3:
    print(f'O MAIOR VALOR DIGITADO FOI: {v2}')
if v3 > v1 and v3 > v2:
    print(f'O MAIOR VALOR DIGITADO FOI: {v3}')
