def voto(ano):
    from datetime import date
    a = date.today().year
    anos = a - ano
    print(f'COM {anos} ANOS: VOTO', end=' ')
    if anos < 16:
        print('NEGADO')
    elif anos >= 16 and anos <= 17 or anos >= 65:
        print('OPCIONAL')
    else:
        print('OBRIGATORIO')

print('-'*25)
voto(int(input('EM QUE ANO VOCE NASCEU? ')))