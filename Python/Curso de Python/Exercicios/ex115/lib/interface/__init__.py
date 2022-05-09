def analizederespostas(n):
    from time import sleep
    resposta = n
    while True:
        resposta = menu(['VER CADASTRADOS', 'CADASTRAR NOVO USUARIO', 'SAIR'])
        if resposta == 1:
            print('OPÇÃO 1')
        elif resposta == 2:
            print('OPÇÃO 2')
        elif resposta == 3:
            print('FINALIZANDO...')
            sleep(1.5)
            cabecalho('ATÉ LOGO!')
            break
        else:
            print('\033[31mERRO!\033[m')
            print('CARREGANDO', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.', end='')
            sleep(0.5)
            print('.')
            sleep(1)
            print('OPÇÃO INVALIDA!')
            print('TENTE NOVAMENTE')
            print()
            print()


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    from ex111.ultilidadecev.dado import leiaint
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSUA OPÇÃO: \033[m')
    return opc