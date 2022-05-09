lista = []

for c in range(0, 5):
    n = int(input('DIGITE UM VALOR: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('ADICIONADO AO FINAL DA LISTA')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'ADICIONADO NA POSIÇAO {pos}')
                break
            pos += 1
print('-='*30)
print(f'OS VALORES DIGITADOS EM ORDEM FORAM {lista}')
