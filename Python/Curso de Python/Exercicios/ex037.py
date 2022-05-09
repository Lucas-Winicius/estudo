print('DIGITE UM NUMERO INTEIRO: ')
v1 = int(input(''))

print('ESCOLHA UMA DAS BASES PARA A CONVERSAO: ')
print('[ 1 ] CONVERTER PARA BINARIO')
print('[ 2 ] CONVERTER PARA OCTAL')
print('[ 3 ] CONVERTER PARA HEXADECIMAL')
v2 = int(input(''))

if v2 == 1:
    print(f'{v1}  CONVERTIDO PARA HEXADECIMAL FICARA {bin(v1)[2:]}')
elif v2 == 2:
    print(f'{v1} CONVERTIDO PARA OCTAL FICARA {oct(v1)[2:]}')
elif v2 == 3:
    print(f'{v1} CONVERTIDO PARA HEXADECIMAL FICARA {hex(v1)[2:]}')
else:
    print('OPCAO INVALIDA TENTE NOVAMENTE')