from time import sleep

v1 = int(input('DIGITE A VELOCIDADE ATUAL DO CARRO: '))

if v1 <= 80:
    print('TENHA UM BOM DIA! DIRIJA COM SEGURANÇA!')
else:
    print('MULTADO! VOCE EXCEDEU O LIMITE DE 80KM/H')
    print(f'VOCE ULTRAPASSOU {v1-80}KM/H ACIMA DO LIMITE PERMITIDO')
    print('VOCE SERA MULTADO!')
    print('CALCULANDO MULTA...')
    sleep(4)
    print(f'SUA MULTA TERA O VALOR DE R${(v1-80)*7}')

