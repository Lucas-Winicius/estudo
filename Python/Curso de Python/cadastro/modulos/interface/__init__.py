def linhas(txt):
    q = len(txt) + 6
    print('~'*q)
    print(f'   {txt}')
    print('~'*q)


def cabecalho(txt):
    print('~'*50)
    print(txt.center(50))
    print('~'*50)