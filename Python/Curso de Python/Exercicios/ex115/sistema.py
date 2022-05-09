from ex115.lib.arquivo import *
from time import sleep
from  ex115.lib.interface import *
from ex111.ultilidadecev.dado import leiaint

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['VER CADASTRADOS', 'CADASTRAR NOVO USUARIO', 'SAIR'])
    if resposta == 1:
        # OPÇÃO PARA LISTAR O CONTEUDO DE UM ARQUIVO
        lerArquivo(arq)
    elif resposta == 2:
        # CADASTRO DE UMA NOVA PESSOA
        cabecalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaint('IDADE: ')
        cadastrar(arq, nome, idade)
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

