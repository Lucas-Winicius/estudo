lista = [[], [], []]
to = 0
ma = 0

for pos in range(0,3):
    for pos2 in range(0, 3):
        v = int(input(f'DIGITE UM VALOR PARA A POSIÇAO [{pos}, {pos2}]: '))
        if v % 2 == 0:
            to = to + v
        if pos == 2:
            if pos2 == 0:
                ma = v
            else:
                if v > ma:
                    ma = v
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
print('-='*35)
print(f'A SOMA DOS VALORES PARES E DE {to}')
print(f'A SOMA DOS VALORES DA TERCEIRA COLUNA E DE {lista[0][2] + lista[1][2] + lista[2][2]}')
print(f'O MAIOR VALOR DA SEGUNDA LINHA E {ma}')
print()
