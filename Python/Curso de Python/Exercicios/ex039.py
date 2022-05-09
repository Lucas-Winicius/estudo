from datetime import date

v1 = date.today().year
v2 = int(input('ANO DE NASCIMENTO: '))

if v1 - v2 == 18:
    print(f'QUEM NASCEU EM {v2} TEM {v1 - v2} ANOS')
    print('VOCE PRECISA SE ALISTAR IMEDIATAMENTE!')
elif v1 - v2 < 18:
    print(f'QUEM NASCEU EM {v2} TEM {v1 - v2} ANOS')
    print(f'VOCE TERA QUE SE ALISTAR EM {18 - (v1 - v2)} ANOS')
elif v1 - v2 > 18:
    print(f'QUEM NASCEU EM {v2} TEM {v1 - v2}')
    print(f'O SEU ALISTAMENTO FOI FEITO EM {v1 - ((v1 - v2) - 18)}')
