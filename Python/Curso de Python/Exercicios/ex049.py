print('-=-'*5)
print('    TABUADA')
print('-=-'*5)

v1 = int(input('DIGITE A TABUADA QUE VOCE DESEJA VER: '))
print('-'*10)
print()
v3 = 0
for v2 in range(0, 11):
    print(f'{v2} X {v3} = {v1 * v3}')
    v3 = v3 + 1
print('-'*10)
