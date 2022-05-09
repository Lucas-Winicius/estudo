dados = dict()
todos = list()

while True:
    dados['nome'] = str(input('NOME: ')).strip().title()
    dados['sexo'] = str(input('SEXO: [M/F] ')).strip().upper()

    if dados['sexo'] != 'M' and dados['sexo'] != 'F':
        while True:
            print('ERRO! RESPONDA APENAS M OU F.')
            dados['sexo'] = str(input('SEXO: [F/M] ')).strip().upper()
            if dados['sexo'] in 'FM':
                break

    dados['idade'] = int(input('IDADE: '))
    todos.append(dados.copy())

    resp = str(input('DESEJA CONTINUAR? [S/N] ')).strip().upper()

    if resp != 'S' and resp != 'N':
        while True:
            print('ERRO! RESPONDA APENAS S OU N.')
            resp = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()
            if resp in 'SN':
                break
    if resp == 'S':
        print()
    else:
        print('FINALIZANDO...')
        break
m = 0
print('-='*35)
print(f'AO TODO TEMOS {len(todos)} PESSOAS CADASTRADAS.')
for c in todos:
    m = m + c['idade']
m = m / len(todos)
print(f'A MEDIA DE IDADE E {m:.2f}')
print('AS MULHERES CADASTRADAS FORAM ', end='')
for c in todos:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print('\nLISTA DAS PESSOAS QUE ESTAO ACIMA DA MÉDIA:')

for c in todos:

    if c['idade'] > m:
        for k, v in c.items():
            print(f'   {k} = {v}, ', end=' ')
        print('\n')
print('<<< ENCERRADO >>>')