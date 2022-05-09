v1 = float(input('VALOR DA CASA: R$'))
v2 = float(input('SALARIO DO COMPRADOR: R$'))
v3 = int(input('QUANTOS ANOS DE FINANCIAMENTO?: '))

if v3 <= 1:
    print(f'PARA PAGAR UMA CASA NO VALOR DE {v1} EM {v3} ANO A PRESTACAO SERA DE R${v1 / (v3 * 12):.2f}')
else:
    print(f'PARA PAGAR UMA CASA NO VALOR DE {v1} EM {v3} ANOS A PRESTACAO SERA DE R${v1 / (v3 * 12):.2f}')

if v1 / (v3 * 12) > 100 / (v2 * 30):
    print('EMPRESTIMO *NEGADO!*')
else:
    print('EMPRESTIMO *APROVADO!*')
