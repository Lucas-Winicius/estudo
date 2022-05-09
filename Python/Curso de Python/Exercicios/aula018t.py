pessoas = [['Pedro', 19], ['Maria', 19], ['João', 32]]



# POSICIONAMENTO DE ELEMENTOS
print(pessoas[0][0]) # ESCREVE OS IDICES DESEJADOS "PEDRO"
print(pessoas[1][1]) # 19
print(pessoas[2][0]) # João
print(pessoas[1]) # ESCREVE TODA A ESTRUTURA DESEJADA ['Maria', 19]

# PARA CRIAR UMA LISTA COMPOSTA
dados = ['Pedro', 25] # LISTA
pessoasco = list() # LISTA VAZIA

pessoasco.append(dados[:]) #ESTRURURA ULTILLIZADA PARA A CRIAÇAO DA LISTA COMPOSTA

#LIMPAR ESTRUTURAS
pessoas.clear()