def leiaint(a):
    while True:
        if a.isnumeric():
            return a
            break
        else:
            print('\033[0;31mERRO! DIGITE UM NUMERO INTEIRO VALIDO.\033[m')
            a = str(input('DIGITE UM NUMERO: '))


#PROGRAMA PRINCIPAL
n = leiaint(input('DIGITE UM NUMERO: '))
print(f'VOCE DIGITOU O NUMERO {n}')