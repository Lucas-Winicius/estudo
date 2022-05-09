def notas(*n, sit=False):
    """
    -> FUNÇÃO PARA ANALIZAR NOTAS E SITUAÇÃOES DE VARIOS ALUNOS.
    :param n: UMA OU MAIS NOTAS DOS ALUNOS (ACEITA VARIAS)
    :param sit: VALOR OPCIONAL, INDICANDO SE DEVE OU NÃO A SITUAÇÃO.
    :return: DICIONARIO COM VARIAS INFORMAÇÕES SOBRE A SITUAÇÃO DA TURMA.
    """
    dados = dict()
    '''cont = 0
    me = 0
    mai = 0
    men = 0

    for c in n:
        me += c
        cont += 1
        if c > mai:
            mai = c
        if cont == 1:
            men = c
        else:
            if c < men:
                men = c

    me = me / cont'''
    dados['total'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['media'] = sum(n) / len(n)
    if sit:
        if dados['media'] >= 9:
            dados['situação'] = 'OTIMA'
        elif dados['media'] >= 7:
            dados['situação'] = 'BOA'
        elif dados['media'] >= 5:
            dados['situação'] = 'REGULAR'
        else:
            dados['situação'] = 'RUIM'
    return dados


resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)