v1 = str(input('Informe o seu sexo: [F/M]')).strip().upper()
while v1 != 'F' and v1 != 'M':
    v1 = str(input('Dados invalidos. Por favor, informe o seu sexo: ')).strip().upper()
print(' ')

if v1 == 'F':
    print('SEXO FEMININO REGISTRADO COM SUCESSO')
else:
    print('SEXO MASCULINO REGISTRADO COM SUCESSO')
