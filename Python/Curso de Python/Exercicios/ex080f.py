lista = []
maior = 0
menor = 0


for c in range(0,5):
    v = int(input(('DIGITE UM VALOR: ')))
    if c == 0:
        print('ADICIONADO NO FINAL DA LISTA...')
        lista.append(v)
        maior = v
    elif c == 1:
        if v > maior:
            print('ADICIONADO NA ULTIMA POSIÇAO...')
            menor = maior
            maior = v
            lista.append(v)
        else:
            menor = v
            print('VALOR ADICIONADO NNO COMEÇO DA LISTA')
    elif c == 2:
        if v > maior:
            v2 = maior
            maior = v
            lista.append(v)
            print('VALOR ADICIONADO NA ULTIMA POSIÇAO')
        elif v < menor:
            v2 = menor
            menor = v
            lista.insert(0, v)
            print('VALOR ADCIONADO NA PRIMEIRA POSIÇAO')
        else:
            v2 = v
            lista.insert(1, v)
            print('VALOR ADICONADO NA POSIÇAO 1')
    elif c == 3:
        if v > maior:
            maior = v
            print('VALOR ADICIONADO NA ULTIMA POSIÇAO')
            lista.append(v)
        elif v < menor:
            menor = v
            print('VALOR ADICIONADO NA PRIMEIRA POSIÇAO')
            lista.insert(0, v)
