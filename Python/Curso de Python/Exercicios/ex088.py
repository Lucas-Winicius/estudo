from random import randint
from time import sleep
numeros = list()
tnum = list()

print('-'*35)
print(f'{"JOGA NA MEGA SENA": ^35}')
print('-'*35)
print()

q = int(input('QUANTOS JOGOS VOCE QUER QUE EU SORTEIE? '))

for c in range(0, q):
    for c2 in range(0, 6):
        while True:
            s = randint(1, 60)
            if s in tnum:
                j = 0
                del(j)
            else:
                tnum.append(s)
                break
    tnum.sort()
    numeros.append(tnum[:])
    tnum.clear()

print()
print('-='*5, f'  SORTEANDO {q} JOGOS  ', '-='*5)
j = 1
sleep(1)
for c3 in numeros:
    print(f'JOGO {j}: {c3}')
    sleep(1.3)
    j += 1
print('-='*6,'   < BOA SORTE >   ', '-='*6)