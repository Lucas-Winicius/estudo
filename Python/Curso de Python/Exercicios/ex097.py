def esc(txt):
    q = len(txt) + 4
    print('~'* q )
    print(f'  { txt}')
    print('~' * q)



esc('Olá, Mundo')