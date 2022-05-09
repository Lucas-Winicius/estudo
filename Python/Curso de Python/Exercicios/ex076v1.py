nomes = 'Lápis', 'Borracha', 'Caderno', 'Estojo', \
        'Transferidor', 'Compasso', 'Mochila', 'Canetas', 'Livro'
precos = 1.75, 2.00, 15.90, 25.00, 4.20, 9.99, 120.32, 22.30, 34.90

print('-'*50)
print(' '*13, 'LISTAGEM DE PREÇOS')
print('-'*50)

pr = -1
for v1 in nomes:
    print(v1, end='')
    contador = len(v1) + 10
    pr = pr + 1

    #PONTILHADO
    for v3 in range(0,50 - len(v1)):
        print('.',end='')
        contador = contador + 1

        #PAUSA O PONTILHADO E POSICIONAMENTO DE PRECOS
        if contador == 50:
            print('R$', precos[pr],'\n')
            break
print('-'*50)