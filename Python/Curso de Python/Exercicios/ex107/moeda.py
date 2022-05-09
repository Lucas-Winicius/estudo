def metade(v, form=False):
    if form:
        rsp = v / 2
        return f'R${rsp:.2f}'.replace('.', ',')
    else:
        return v / 2


def dobro(v, form=False):
    if form:
        rsp = v * 2
        return f'R${rsp:.2f}'.replace('.', ',')
    else:
        return v * 2


def aumentar(v, a, form=False):
    rsp = ((v * a) / 100) + v
    if form:
        return f'R${rsp:.2f}'.replace('.', ',')
    else:
        return rsp


def diminuir(v, a, form=False):
    rsp = v - ((v * a) / 100)
    return rsp if form is False else moeda(rsp)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo(p=0, a=0, r=0):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)

    print(f'{"PREÇO ANALIZADO:":<20}', end='')
    print(f'{moeda(p):>10}')

    print(f'{"DOBRO DO PREÇO:":<20}', end='')
    print(f'{dobro(p, form=True):>10}')

    print(f'{"METADE DO PREÇO:":<20}', end='')
    print(f'{metade(p, form=True):>10}')


    print(f'{a}{"% DE AUMENTO:":<18}', end='')
    print(f'{aumentar(p, a, form=True):>10}')

    print(f'{r}{"% DE REDUÇÃO:":<18}', end='')
    print(f'{diminuir(p, r, form=True):>10}')

    #print(f'{r}% DE REDUÇÃO: \t{diminuir(p, r, form=True)}')
    print('-'*30)