dados = dict()
gols = list()

dados['Nome'] = str(input('NOME DO JOGADOR: ')).strip().title()
p = int(input(f'QUANTAS PARTIDAS {dados["Nome"]} JOGOU? '))

cont = 0
for c1 in range(1, p+1):
    p = int(input(f'QUANTOS GOLS {dados["Nome"]} FEZ NA {c1}ª PARTIDA? '))
    gols.append(p)
    cont += p

dados['gols'] = gols
dados['Total'] = cont

print('-='*35)
print(dados)
print('-='*35)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-='*35)
for p, g in enumerate(gols):
    print(f'    => NA PARTIDA {p + 1}, FEZ {g} GOLS.')
print(f'FOI UM TOTAL DE {dados["Total"]} GOLS.')