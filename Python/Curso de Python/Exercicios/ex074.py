from random import randint

n = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))
print(f'OS NUMEROS SORTEADOS FORAM {n}')
n = sorted(n)
print(f'O MENOR VALOR SORTEADO FOI {n[0]}')
print(f'O MAIOR VALOR DIGITADO FOI {n[-1]}')

'''print(n)
print(f'O maior valor é {max(n)} e o menor é {min(n)}.')'''

