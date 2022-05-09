from random import randint

t = 0
chute = ''
senha = str(input('Digite uma senha: ')).strip()

cac = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
'@', '!', '#', '$', '&', '*', '(', ')', '-', '_', '[', ']', '{', '}', '<', '>', 'ç', 'Ç', '+', '~', '=', ' ',
'1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

#print(len(cac))

#84
while chute != senha:
    chute = ''
    t += 1
    for letra in senha:
        acho = cac[randint(0, 83)]
        chute = str(acho) + str(chute)
    print(chute)

print(f'Senha encontrada {chute}')
print(f'Numero de tentativas: {t}')
