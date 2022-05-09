v3 = 0

v1 = int(input('DIGITE UM NUMERO: '))

for v2 in range(1, v1+1):
    if v1 % v2 == 0:
        v3 = v3 + 1

if v3 == 2:
    print(f'O NUMERO {v1} E PRIMO')
else:
    print(f'O NUMERO {v1} NAO E PRIMO')

