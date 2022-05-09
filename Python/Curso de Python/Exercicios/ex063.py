n1 = 0
n2 = 1

print('-'*35)
print(' '*5, 'SEQUENCIA DE FIBONACCI')
print('-'*35)
print()

t = int(input('QUANTOS TERMOS VOCE QUER MOSTRAR? '))

while t >= 1:
    t = t - 2
    print(n1, end=' → ')
    n1 = n1 + n2
    print(n2, end=' → ')
    n2 = n2 + n1
