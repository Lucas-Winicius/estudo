co1 = 0
co2 = 0

from datetime import date
v1 = date.today().year

for v2 in range(1, 8):
    v3 = int(input(f'ANO EM QUE A {v2}ª PESSOA NASCEU: '))
    if v1 - v3 < 18:
        co1 = co1 + 1
    else:
        co2 = co2 + 1

print('')

print(f'AO TODO TIVEMOS {co2} PESSOAS MAIORES DE IDADE')
print(f'E TAMBEM TIVEMOS {co1} PESSOAS MENORES DE IDADE')
