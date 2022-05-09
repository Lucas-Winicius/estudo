to = 0
while True:

    print('-'*30)
    t = int(input('QUER VER A TABUADA DE QUAL VALOR? '))
    print('-'*30)
    if t <=0:
        break
    for v1 in range(0, 11):
        print(f'{t} X {v1} = {t * v1}')
    to = to + 1
print(f'VOCE SOLICITOU {to} TABUADAS')
print('OBRIGADO(A) POR ULTILIZAR NOSSO PROGRAMA')
print('-'*30)