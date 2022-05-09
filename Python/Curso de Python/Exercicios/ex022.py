v1 =  input(('DIGITE O SEU NOME COMPLETO: ')).strip()

print('ANALIZANDO O SEU NOME...')

print(f'SEU NOME EM LETRAS *MAIUSCULAS* FICA {v1.upper()}')
print(f'SEU NOME EM LETRAS *minusculas* FICA {v1.lower()}')
print(f'SEU NOME AO TODO TEM {len(v1.split())} LETRAS')
v2 = v1.split()
print(f'SEU PRIMEIRO NOME TEM {len(v2[0])}')