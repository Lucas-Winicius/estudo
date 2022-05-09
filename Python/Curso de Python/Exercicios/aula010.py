v1 = float(input('DIGITE A SUA PRIMEIRA NOTA: '))
v2 = float(input('DIGITE A SUA SEGUNDA NOTA: '))
v3 = (v1+v2) / 2

if v3 <= 6.0:
    print('SUA NOTA ESTA BAIXA ESTUDE MAIS NA PROXIMA')

else:
    print('PARABENS VOCE ESTA COM UMA BOA MEDIA')

print(f'SUA MEDIA FOI {v3:.1f}')


#n = str(input('QUAL O SEU NOME? '))
#if n == 'ABOBORA':
#    print('OLA VEGETALLIS')
#else:
#    print('VOCE NAO ME PARECE UM VEGETAL')
#print(f'HOLA {n}')
