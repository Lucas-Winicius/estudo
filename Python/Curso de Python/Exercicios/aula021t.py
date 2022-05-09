# CRIAR UMA DESCRIÇAO PARA A SUA DEF
'''def contador(i, f, p):# ABRIR 3 " DULPLAS E DAR ENTER
    """"
    -> FAZ UMA CONTAGEM E MOSTRA NA TELA.
    :param i: INICIO DA CONTAGEM
    :param f: FIM DA CONTAGEM
    :param p: PASSO DA CONTAGEM
    :return: SEM RETORNO
    Function created BY: Abobora
    """
    c = i
    while c <= f:
        print(c, end=' ')
        c += p
    print('FIM!')

contador()
help(contador)'''


# VARIAVEIS OPCIONAIS
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A SOMA VALE {s}')

somar()'''

# ESCOPO DE VARIAVEIS
'''def teste():
    x = 8 # ESSA VARIAVEL SO FUNCIONARA DENTRO DESSA def CHAMADA: VARIAVEL DE ESCOPE LOCAL
    print(f'NA FUNÇAO TESTE, n VALE {n}')
    print(f'NA FUNÇAO TESTE, x VALE {x}')


n = 2 #VARIAVEL COM ESCOPE GLOBAL FUNCIONARA EM QUALQUER LOCAL DO PROGRAMA
print(f'NO PROGRAMA PRINCIPAL, n VALE {n}')
print(f'NO PROGRAMA PRINCIPAL, x VALE {x}')'''

# ESCOPO GLOBAL DENTRO DE DEF
'''def teste(b):
    global a #PARA SOLICITAR O VALOR GLOBAL E NAO CRIAR UMA NOVA VARIAVEL CHAMADA A
    a = 8
    b += 4
    c = 2
    print(f'*A* DENTRO VALE {a}')
    print(f'*B* DENTRO VALE {b}')
    print(f'*C* DENTRO VALE {c}')

a = 5
teste(a)
print(f'*A* FORA VALE {a}')'''


# VARIAVEIS RETURN
'''def somar(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)

print(f'OS RESULTADOS FORAM {r1}, {r2}, {r3}')'''
