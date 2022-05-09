time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('NOME DO JOGADOR: ')).strip().title()
    tot = int(input(f'QUANTAS PARTIDAS {jogador["nome"]} JOGOU? '))
    partidas.clear()
    for c in range(1, tot + 1):
        partidas.append(int(input(f'    QUANTOS GOLS NA PARTIDA {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        rsp = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()[0]
        if rsp in 'SN':
            break
        print('ERRO! RESPONDA APENAS S OU N')
    if rsp == 'N':
        break
print('-='*35)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)

while True:
    bsc = int(input('MOSTRAR DADOS DE QUAL JOGADOR? (999 PARA PARAR)'))
    if bsc == 999:
        break
    if bsc >= len(time):
        print(f'NAO EXISTE O JOGADOR CPM CODIGO {bsc}')
    else:
        print(f'  -- LEVANTAMENTO DO JOGADOR {time[bsc]["nome"]}:')
        for i, g in enumerate(time[bsc] ['gols']):
            print(f'   NO JOGO {i+1} FEZ {g} GOLS')
    print('-'*40)
print('<<< VOLTE SEMPRE >>>')
