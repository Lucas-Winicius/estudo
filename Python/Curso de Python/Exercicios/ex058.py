t = 0
r = 'false'

from random import randint

print('-' * 30)
print('     JOGO DA ADIVINHAÇAO')
print('-' * 30)
print('EU SOU O COMPUTADOR....')
print('')
print('ACABEI DE PENSAR EM UM NUMERO ENTRE 0 E 250.')
print('')
print('SERA QUE VOCE CONSEGUE PENSAR EM QUAL FOI?')
print('')

n = randint(0, 250)
p1 = int(input('QUAL O SEU PALPITE? '))

while r != 'true':
    if p1 == n:
        r = 'true'
    elif p1 < n:
        print('MAIS... TENTE MAIS UMA VEZ.')
        p1 = int(input('QUAL O SEU PALPITE? '))
    elif p1 > n:
        print('MENOS... TENTE MAIS UMA VEZ')
        p1 = int(input('QUAL O SEU PALPITE? '))
    t = t + 1
print('')
print('-' * 20)
print(f'ACERTOU COM {t} TENTATIVAS. PARABENS')
print('-' * 20)
