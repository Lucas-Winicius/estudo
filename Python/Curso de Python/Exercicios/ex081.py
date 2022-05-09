lista = list()
while True:
    v = int(input('DIGITE UM VALOR: '))
    lista.append(v)
    c = str(input('DESEJA CONTINUAR [S/N]: ')).strip().upper()
    if c == 'S':
        print()
    elif c == 'N':
        print('FINALIZANDO...')
        break
    else:
        print('COMANDO INVALIDO')
        print('TENTE OUTRA VEZ')
        print('FINALIZANDO . . .')
        break
print('-='*35)
lista.sort(reverse=True)
print(f'VOCE DIGITOU {len(lista)} VALORES')
print(f'OS VALORES NA ORDEM DECRECENTE SÃO {lista}')
if 5 in lista:
    print('O VALOR 5 FAZ PARTE DA LISTA')
else:
    print('O VALOR 5 NAO FAZ PARTE DA LISTA')
