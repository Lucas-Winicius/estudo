dados = list()


while True:
    nome = str(input('NOME: ')).strip().title()
    n1 = float(input('NOTA 1: '))
    n2 = float(input('NOTA 2: '))
    media = (n1 + n2) / 2
    dados.append([nome, [n1, n2], media])
    resp = str(input('DESEJA CONTINUAR? [S/N] ')).strip().title()

    if resp == 'S':
        print()
    elif resp == 'N':
        print('FINALIZANDO...')
        print()
        break
    else:
        print('COMANDO INVALIDO')
        print('FINALIZANDO...')
        print()
        break
print()
print('-='*30)
print(f'{"NO.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    n = int(input('MOSTRAR NOTAS DE QUAL ALUNO? [999 PARA PARAR] '))
    print()
    if n == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    elif n > i:
        print('HEY, NAO TENHO DADOS SOBRE ESSE ALUNO!')
        print('TENTE NOVAMENTE')
        print(f'LEMBRE-SE OS "NO." VAO DE 0 A {i}')
        print()
    else:
        print(f'AS NOTAS DE {dados[n][0]} SÃO {dados[n][1]}')
        print()
