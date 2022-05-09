'''def mostralinha():
    print('-'*50)



mostralinha()
print(f'{"OLÁ, MUNDO!": ^50}')
mostralinha()'''


'''def titulo(txt):
    print('-'*30)
    print(txt)
    print('-'*30)
    print()


titulo('   CURSO EM VIDEO')
titulo('OI')
titulo('PYTHON E MUITO BOM')'''


'''def soma(a, b):
    s = a + b
    print(s)


soma(1, 3, 5)

# E POSSIVEL TROCAR A POSIÇAO DOS VALORES
soma(b=5, a=7)'''


'''def contador(* num):
    tot = 0
    for valor in num:
       tot += valor
    print(tot)


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)'''


'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)'''