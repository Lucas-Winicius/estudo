# ESCREVE NOME E IDADE
'''galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]

for l in galera:
    print(f'{l[0]} TEM {l[1]} ANOS DE IDADE')'''

galera = list()
dados = list()

for c in range(0, 3):
    dados.append(str(input('NOME: ')))
    dados.append((int(input('IDADE: '))))
    galera.append(dados[:])
    dados.clear()
print(galera)