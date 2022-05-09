from logica import *
from interface import *

linha('Sitema de cadastro')

opcs(['Cadastrar', 'Ver usuarios', 'Trocar informações', 'Sair'])

while True:
        opc = int(ler_int('Sua opção: '))

        if opc == 1:
            cadastrar()
            break

        elif opc == 2:
            usr = ver_user(msg=True)
            opcs(usr)
            break

        elif opc == 3:
            print('Opção indisponivel!')
            break

        elif opc == 4:
            print('Saindo...')
            print('Obrigado por usar nossos serviços')
            sleep(3)
            print('Volte sempre!')
            print()
            break
        else:
            print('Opção Invalida!')