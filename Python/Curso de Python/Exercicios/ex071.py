n50 = 0
n10 = 0
n1 = 0

print('='*30)
print(' '*5, 'BANCO NOVO FUTURO')
print('='*30)
print()

v = int(input('QUE VALOR VOCE QUER SACAR?'))

'''while True:
    if v - 50 >= 50:
        v = v - 50
        n50 = n50 + 1
    else:
        break

while True:
    if v - 10 >= 10:
        v = v - 10
        n10 = n10 + 1
    else:
        break

while True:
    if v - 1 >= 0:
        v = v - 1
        n1 = n1 + 1
    else:
        break'''

while v > 49:
    v = v - 50
    n50 = n50 + 1

while v > 9:
    v = v - 10
    n10 = n10 + 1

while v > 0:
    v = v - 1
    n1 = n1 + 1

print(f'TOTAL DE {n50} CEDULAS DE R$50')
print(f'TOTAL DE {n10} CEDULAS DE R$10')
print(f'TOTAL DE {n1} CEDULAS DE R$1')