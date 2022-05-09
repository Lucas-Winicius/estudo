c = 0
n2 = 0
p = 1

while p != 0:
    n1 = int(input('DIGITE UM NUMERO [999 PARA PARAR]: '))
    if n1 == 999:
        p = 0
    else:
        n2 = n2 + n1
        c = c + 1
print(f'VOCE DIGITOU {c} VALORES A SOMA ENTRE ELES FOI DE {n2}')
