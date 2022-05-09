def maior(* num):
    ma = 0
    for c in num:
        if c > ma:
            ma = c
    print('-='*25)
    print('ANALIZANDO OS VALORES PASSADOS...')
    for c in num:
        print(c, end=' ')
    print(f'\nFORAM INFORMADOS {len(num)} VALORES AO TODO')
    print(f'O MAIOR VALOR INFORMADO FOI {ma}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)