lista = [[], []]
for c in range(1,8):
    n = int(input(f'DIGITE O {c}º VALOR: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

lista[0].sort()
lista[1].sort()

print()
print(f'OS VALORES PARES DIGITADOS FORAM {lista[0]}')
print(f'OS VALORES IMPARES DIGITADOS FORAM {lista[1]}')
print()
