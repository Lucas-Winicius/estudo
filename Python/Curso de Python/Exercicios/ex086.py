lista = [[], [], []]

for pos in range(0,3):
    for pos2 in range(0, 3):
        v = int(input(f'DIGITE UM VALOR PARA A POSIÇAO [{pos}, {pos2}]: '))
        lista[pos].append(v)
print('-='*35)
for c in lista:
    cont = 0
    for c1 in c:
        cont = cont + 1
        if cont < 3:
            print(f'[{c1: ^5}]', end='')
        else:
            print(f'[{c1: ^5}]\n')