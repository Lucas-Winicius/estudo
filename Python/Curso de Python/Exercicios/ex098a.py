from time import  sleep


def contador(i, f, p):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('-='*20)
    print(f'CONTAGEM DE {i} ATE {f} DE {p} EM {p}')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= p
        print('FIM')


#PROGRAMA PRINCIPAL
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('AGORA EA SUA VEZ DE PERSONALIZAR COMANDOS!')
ini = int(input('INICIO: '))
fin = int(input('FIM: '))
pas = int(input('PASSO: '))
contador(ini, fin, pas)