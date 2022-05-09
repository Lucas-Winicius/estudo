from random import randint
numeros = list()


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(1, 10))
    print('SORTEANDO 5 VALORES DA LISTA:', end=' ')
    for c in numeros:
        print(c, end=' ')
    print('PRONTO!')


def somapar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma = soma + c
    print(f'SOMANDO OS VALORES PARES DE {numeros}, TEMOS {soma}')


sorteia()
somapar()
