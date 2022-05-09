from datetime import date
v1 = date.today().year

v2 = int(input('ANO DE NASCIMENTO: '))

v3 = v1 - v2

if v3 < 9:
    print(f'O ATLETA TEM {v3} ANOS')
    print('CLASSIFICAÇAO: MIRIM')
elif v3 <= 14 and v3 > 9:
    print(f'O ATLETA TEM {v3} ANOS')
    print('CLASSIFICAÇAO: INFANTIL')
elif v3 <= 19 and v3 > 14:
    print(f'O ATLETA TEM {v3} ANOS')
    print('CLASSIFICAÇAO: JÚNIOR')
elif v3 <= 25 and v3 > 19:
    print(f'O ATLETA TEM {v3} ANOS')
    print('CLASIFICAÇAO: SÊNIOR')
elif v3 >= 25:
    print(f'O ATLETA TEM {v3} ANOS')
    print('CLASSIFICAÇAO: SÊNIOR')
else:
    print(f'O ATLETA TEM {v3} ANOS')
    print('HOUVE UM ERRO INTERNO')
