maior = 0
menor = 0

for v1 in range(1, 6):
    peso = float(input(f'PESO DA {v1}ª PESSOA: '))
    if v1 == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O MAIOR PESO LIDO FOI DE {maior}Kg')
print(f'O MENOR PESO LIDO FOI DE {menor}Kg')
