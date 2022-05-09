import random

a1 = input('PRIMEIRO ALUNO: ')
a2 = input('SEGUNDO ALUNO: ')
a3 = input('TERCEIRO ALUNO: ')
a4 = input('QUARTO ALUNO: ')
a5 = [a1, a2, a3, a4]

print(f'O ALUNO ESCOLHODO FOI {random.choice(a5)}')
