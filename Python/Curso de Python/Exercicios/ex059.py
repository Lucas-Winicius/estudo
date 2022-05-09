from time import sleep

n1 = 0
n2 = 0
op = 'falso'

while op != 'VERDADEIRO':
    n1 = float(input('Primeiro valor: '))
    n2 = float(input('Segundo valor: '))
    print('-=-'*20)
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR ')
    print('[ 4 ] DIVISAO')
    print('[ 5 ] NOVOS VALORES')
    print('[ 6 ] SAIR')
    op2 = int(input('Qual a sua opçao? '))
    print('-=-'*20)
    if op2 == 1:
        print(f'A SOMA ENTRE {n1:.1f} + {n2:.1f} RESULTA EM *{n1 + n2}*')
    elif op2 == 2:
        print(f'O RESULTADO DE {n1:.1f} X {n2:.1f} RESULTA EM *{n1 * n2}*')
    elif op2 == 3:
        m = 0
        if n1 < n2:
            print(f'ENTRE {n1} E {n2} O MAIOR E {n2}')
        elif n1 > n2:
            print(f'ENTRE {n1} E {n2} O MAIOR E {n1}')
        elif n1 == n2:
            print('OS VALORES SAO IGUAIS')
    elif op2 == 4:
        print(f'A DIVISAO ENTRE {n1} / {n2} RESULTA EM *{n1 / n2}*')
    elif op2 == 5:
        print('INFORME OS NUMEROS NOVAMENTE!')
    elif op2 == 6:
        op = 'VERDADEIRO'
        print('FINALIZANDO...')
        sleep(2)
    print('-=-'*20)
print(' ')
print('PROGRAMA FINALIZADO!')