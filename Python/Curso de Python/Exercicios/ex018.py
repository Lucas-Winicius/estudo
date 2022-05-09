import math

v2 = float(input('DIGITE O ANGULO QUE VOCE DESEJA: '))
v1 = math.radians(v2)

print(f'O ANGULO DE {v1} TEM O SENO DE {math.sin(v1):.2f}')
print(f'O ANGULO DE {v1} TEM O COSENO DE {math.cos(v1):.2f}')
print(f'O ANGULO DE {v1} TEM A TANGENTE DE {math.tan(v1):.2f}')
