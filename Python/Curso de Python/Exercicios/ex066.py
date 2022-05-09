n = 0
s = 0
c = 0
while True:
    n = int(input('DIGITE UM NUMERO [999 PARA PARAR]: '))
    if n == 999:
        break
    s = s + n
    c = c + 1
print(f'A SOMA DESSES {c} FOI DE {s}')
