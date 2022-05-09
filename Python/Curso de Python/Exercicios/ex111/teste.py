import moeda

p = float(input('DIGITE UM PREÇO: R$'))
print(f'A METADE DE {moeda.moeda(p)} É {moeda.metade(p, form=True)}')
print(f'O DOBRO DE {moeda.moeda(p)} É {moeda.dobro(p, form=True)}')
print(f'AUMENTANDO 10%, TEMOS {moeda.aumentar(p, 10, form=True)}')
print(f'DIMINUINDO 13%, TEMOS {moeda.diminuir(p, 13, form=True)}')
