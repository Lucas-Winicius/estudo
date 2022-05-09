lista = list()

for c in range(0, 5):
    lista.append(int(input(f'DIGITE UM VALOR PARA A POSIÇÃO {c + 1}: ')))
print('-='*25)
print('VOCE DIGITOU OS VALORES: ', end='')

for c in lista:
    print(c, end='-')
print('\n')

lista1 = lista[:]
lista1.sort(reverse=True)

print(f'O MAIOR VALOR DIGITADO FOI {lista1[0]} NAS POSIÇÕES ', end='')

for c, c1 in enumerate(lista):
    if c1 == lista1[0]:
        print(f'{c + 1}...', end=' ')

print('\n')

lista1.sort()
print(f'O MENOR VALOR DIGITADO FOI {lista1[0]} NAS POSIÇÕES ', end='')

for c, c1 in enumerate(lista):
    if c1 == lista1[0]:
        print(f'{c + 1}...', end=' ')
