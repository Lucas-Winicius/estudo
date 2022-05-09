def ficha(nome='<Desconhecido>', gols=0):
    if nome.strip() == '':
        nome = '<Desconhecido>'
    if g.isnumeric():
        gols = (int(g))
    else:
        gols = 0
    print(f'O JOGADOR {nome} FEZ {gols} GOLS')


print('-'*25)
n = str(input('NOME DO JOGADOR: ')).strip().title()
g = str(input('NUMERO DE GOLS: '))

ficha(n, g)
