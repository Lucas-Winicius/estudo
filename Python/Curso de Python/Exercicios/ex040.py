v1 = float(input('PRIMEIRA NOTA: '))
v2 = float(input('SEGUNDA NOTA: '))

if (v1 + v2) / 2 >= 7.0:
    print(f'TIRANDO {v1} E {v2} A MEDIA SERA DE {(v1 + v2) / 2}')
    print('ALUNO APROVADO!')
elif (v1 + v2) / 2 < 5.0:
    print(f'TIRANDO {v1} E {v2} A MEDIA SERA DE {(v1 + v2) / 2}')
    print('ALUNO REPROVADO!')
else:
    print(f'COM AS NOTAS {v1} E {v2} A MEDIA SERA DE {(v1 + v2) / 2}')
    print('ALUNO EM RECUPERACAO!')