v2 = 0
v3 = 0
for v1 in range(1, 501, 2):
    if v1 % 3 == 0:
        #print(v1, end=' ')
        v2 = v2 + v1
        v3 = v3 + 1
print(f'A SOMA DE TODOS OS {v3} VALORES E DE {v2}')
