lista = list()

while True:
    v = int(input('DIGITE UM VALOR: '))
    print()
    if v in lista:
        print('O VALOR DUPLICADO')
        print(f'NAO IREI ADICIONAR O  VALOR {v}')
        co = str(input('DESEJA CONTINUAR [S/N]: '))
        if co == 'S':
            print('ENTENDIDO!')
            print()
        elif co == 'N':
            print('FINALIZANDO...')
            break
        else:
            print('COMANDO INVALIDO')
            print('POR ESSE MOTIVO FINALIZAREMOS O PROCESSO')
            print('FINALIZANDO...')
            break
    else:
        lista.append(v)
        print('VALOR ADICIONADO COM SUCESSO')
        co = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
        if co == 'S':
            print('ENTENDIDO!')
            print()
        elif co == 'N':
            print('FINALIZANDO...')
            break
        else:
            print('COMANDO INVALIDO')
            print('POR ESSE MOTIVO FINALIZAREMOS O PROCESSO')
            print('FINALIZANDO...')
            break
print('-'*35)
lista.sort()
print(f'VOCE DIGITOU OS VALORES {lista}')
