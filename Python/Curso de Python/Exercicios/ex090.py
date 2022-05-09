dados = dict()

dados['nome'] = str(input('NOME: ')).strip().title()
dados['media'] = float(input(f'MEDIA DE {dados["nome"]}: '))

print('-='*35)
print(f"  - NOME E IGUAL A {dados['nome']}")
print(f"  - MEDIA E IGUAL A {dados['media']:.1f}")
print('  - SITUAÇAO E IGUAL A ', end='')

if dados['media'] < 5:
    print('REPROVADO')
elif dados['media'] >= 7 and dados['media'] <= 10:
    print('APROVADO')
elif dados['media'] > 10:
    print('\n  - ERRO...')
    print('  - NOTA INVALIDA!')
    print('  - TENTE DIGITAR UMA NOTA INFERIOR OU IGUAL A 10')
else:
    print('RECUPERAÇÃO')