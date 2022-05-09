import math

c1 = float(input('COMPRIMENTO DO CATETO OPOSTO: '))
c2 = float(input('COMPRIMENTO DO CATETO ADJACENTE: '))

print(f'A HIPOTENUSA VAI MEDIR {math.hypot(c1, c2):.2f}')
