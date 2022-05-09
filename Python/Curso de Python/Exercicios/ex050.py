v2 = 0
for v1 in range(0, 6):
    n1 = int(input('DIGITE UM NUMERO: '))
    if n1 % 2 == 0:
        v2 = v2 + n1
print(f'A SOMA DE TODOS OS VALORES EQUIVALE A {v2}')