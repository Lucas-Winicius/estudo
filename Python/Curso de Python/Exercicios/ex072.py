nomes = ('ZERO', 'UM', 'DOIS', 'TRÊS', 'QUATRO', 'CINCO', 'SEIS', 'SETE', 'OITO', 'NOVE', 'DEZ', 'ONZE', 'DOZE', 'TREZE', 'QUATORZE OU CATORZE', 'QUINZE', 'DEZESSEIS', 'DEZESSETE', 'DEZOITO', 'DEZENOVE', 'VINTE')

n = int(input('DIGITE UM NUMERO ENTRE 0 E 20: '))
print()

while True:
    if n > 20:
        print('NUMERO INVALIDO')
        print('ACEITAMOS APENAS NUMEROS INFERIORES A 20')
        print('TENTE NOVAMENTE...')
        print()
        n = int(input('DIGITE OUTRO NUMERO INFERIOR A 20: '))
    elif n < 0:
        print('NUMERO INVALIDO')
        print('TENTE NOVAMENTE')
        print('TENTE NOVAMENTE DESTA VEZ COM UM NUMERO SUPERIOR A 0')
        print()
        n = int(input('TENTE NOVAMENTE: '))
    else:
        print(f'O NUMERO {n} POR EXTENSO ELE FICA "{nomes[n]}"')
        break
del(n)
del(nomes)
print()
print('FIM DO PROGRAMA.')
