frase = str(input('DIGITE UMA FRASE: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'O INVERSO DE {frase} È {inverso}')

if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    print('A FRASE DIGITADA NAO GERA UM PALINDRIMO')
