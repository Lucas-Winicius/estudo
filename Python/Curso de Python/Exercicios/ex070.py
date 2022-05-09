m = 999999999999999999999
t = 0
ca = 0
nm = 'Oi'

print('-'*45)
print(' '*11, 'LOJA SUPER PUMPIKIN')
print('-'*45)
print()

while True:
    print('-'*30)
    n = str(input('NOME DO PRODUTO: ')).strip()
    p = float(input('PREÇO: R$'))
    con = str(input('QUER CONTINUAR? [S/N] ')).strip().upper()
    print('-'*30)


    if p < m:
        m = p
        nm = n
    t = t + p

    if p > 1000:
        ca = ca + 1

    if con == 'N':
        print('FINALIZED...')
        print()
        break

print('CALCULANDO...')
print(f'O TOTAL DA COMPRA FOI DE R${t:.2f}')
print(f'TEMOS {ca} CUSTANDO MAIS QUE R$1000.00')
print(f'O PRODUTO MAIS BARATO FOI A {nm} QUE CUSTOU R${m:.2f}')
