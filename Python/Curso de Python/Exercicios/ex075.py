n1 = int(input(('DIGITE UM NUMERO: ')))
n2 = int(input('DIGITE OUTRO NUMERO: '))
n3 = int(input('DIGITE MAIS UM NUMERO: '))
n4 = int(input('DIGITE O ULTIMO NUMERO: '))

dados = (n1, n2, n3, n4)
del(n1, n2, n3, n4)

#o maior
n1 = sorted(dados)
n1 = n1[-1]

print()
print(f'VOCE DIGITOU OS VALORES {dados}')
print()
print(f'O VALOR {n1} APARECEU {dados.count(n1)} VEZES')
del(n1)
print()

#o menor
n1 = sorted(dados)
n1 = n1[0]

#contagem do menor
print(f'O VALOR {n1} APARECEU NA POSIÇAO {dados.index(n1)+1}')
del(n1)

#contagem de pares
n1 = 0
for c1 in dados:
    if c1 % 2 == 0:
        n1 += 1

print(f'FORAM DIGITADOS {n1} VALORES PARES')
del(n1, dados)