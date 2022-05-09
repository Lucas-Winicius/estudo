t = 0
th = 0
tm = 0

while True:
    print('-'*30)
    print(' '*4, 'CADASTRE UMA PESSOA')
    print('-'*30)
    print()

    print('-'*35)
    n = input('NOME: ')
    i = int(input('IDADE: '))
    s = str(input('SEXO: [F/M] ')).strip().upper()
    c = str(input('QUER CONTINUAR: [S/N]')).strip().upper()
    print('-'*35)

    if i > 18:
        t = t + 1

    if s == 'M':
        th = th + 1

    if s == 'F' and i < 20:
        tm = tm + 1
    if c == 'N':
        break

print(f'TOTAL DE PESSOAS COM MAIS DE 18 ANOS: {t}')
print(f'AO TODO TEMOS {th} HOMENS CADASTRADOS')
print(f'TEMOS {tm} MULHERES COM MENOS DE 20 ANOS')