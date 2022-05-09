def area(a, b):
    s = a * b
    print(f'A AREA DE UM TERRENO DE {a} X {b} E DE {s:.2f}M²')


print('-'*20)
print('CONTROLE DE TERRENOS')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print()
area(l, c)