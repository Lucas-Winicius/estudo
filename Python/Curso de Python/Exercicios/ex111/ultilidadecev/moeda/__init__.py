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
    print('\033[7;30;47m-\033[m'*30)
    print('\033[7;30;47m       RESUMO DO VALOR        \033[m')
    print('\033[7;30;47m-\033[m'*30)

    print(f'\033[7;30;47m{"PREÇO ANALIZADO:":<20}\033[m', end='')
    print(f'\033[7;30;47m{moeda(p):>10}\033[m')

    print(f'\033[7;30;47m{"DOBRO DO PREÇO:":<20}\033[m', end='')
    print(f'\033[7;30;47m{dobro(p, form=True):>10}\033[m')

    print(f'\033[7;30;47m{"METADE DO PREÇO:":<20}\033[m', end='')
    print(f'\033[7;30;47m{metade(p, form=True):>10}\033[m')


    print(f'\033[7;30;47m{a}{"% DE AUMENTO:":<18}\033[m', end='')
    print(f'\033[7;30;47m{aumentar(p, a, form=True):>10}\033[m')

    print(f'\033[7;30;47m{r}{"% DE REDUÇÃO:":<18}\033[m', end='')
    print(f'\033[7;30;47m{diminuir(p, r, form=True):>10}\033[m')

    #print(f'{r}% DE REDUÇÃO: \t{diminuir(p, r, form=True)}')
    print('\033[7;30;47m-\033[m'*30)