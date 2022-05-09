from random import randint
from time import sleep

print('-=-'*17)
print(' VOU PENSAR EM UM NUMERO DE 0 A 5 TENTE ADIVINHAR')
print('-=-'*17)
print(' ')

v1 = randint(0, 5)
v2 = int(input('EM QUE NUMERO PENSEI? '))
print('PROCESSANDO...')
print(' ')
sleep(3)

if v1 == v2:
    print('PARABENS VOCE E UM ADVINHADOR PROFISSIONAL')
    print('VOCE GANHOU!')

else:
    print(f'QUE PENA EU PENSEI NO NUMERO {v1} E VOCE NO {v2}')
    print('TENTE NOVAMENTE E BOA SORTE')

