v1 = str(input('DIGITE O SEU NOME COMPLETO: ')).strip()
v2 = v1.split()

print(f'PRAZER TE CONHECER *{v2[0]}*')
print(f'SEU PRIMEIRO NOME E {v2[0]}')
print(f'SEU ULTIMO NOME E {v2[len(v2)-1]}')