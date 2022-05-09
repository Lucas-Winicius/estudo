from  datetime import date
a = date.today().year

dados = dict()

dados['Nome'] = str(input('NOME: ')).strip().title()
dados['Idade'] = int(input('ANO DE NASCIMENTO: '))
dados['Idade'] = a - dados['Idade']

a = int(input('CARTEIRA DE TRABALHO  (0 NÃO TEM): '))

if a != 0:
    dados['ctps'] = a
    dados['Contrataçao'] = int(input('ANO DE CONTRATAÇAO: '))
    dados['Salario'] = float(input('SALÁRIO: '))
    dados['Aposentadoria'] = dados['Idade '] + ((dados['Contrataçao'] + 35) - date.today().year)

print('-='*35)
for k, i in dados.items():
    print(f'   - {k}: {i}')