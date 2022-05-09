def esc(txt):
    q = len(txt) + 4
    print('~'* q )
    print(f'  { txt}')
    print('~' * q)


while True:
    esc('SISTEMA DE AJUDA PyHELP')
    a = str(input('FUNÇÃO OU BIBLIOTECA > ')).strip().lower()
    if a == 'fim':
        esc('ATE LOGO !')
        break
    else:
        help(a)
