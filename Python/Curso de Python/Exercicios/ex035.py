print('-='*20)
print('       ANALIZADOR DE TRIANGULOS')
print('-='*20)

v1 = float(input('DIGITE O PRIMEIRO SEGMENTO: '))
v2 = float(input('DIGITE O SEGUNDO SEGMENTO: '))
v3 = float(input('DIGITE O TERCEIRO SEGMENTO: '))

if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('OS SEGMENTOS PODEM FORMAR UM TRIANGULO!')
else:
    print('OS SEGMENTOS NAO PODEM FORMAR UM TRIANGULO!')
