# COMO CRIAR E MODIFICAR ARQUIVOS:
valores_celurares = [850, 2230, 1500, 3500, 5000]

# Funções do with #

# 'r'  -> Usado somente para ler algo 
# 'w'  -> Usado somente para escrever algo
# 'r+' -> Usado para ler e escrever algo
# 'a'  -> Usado para acresentar algo


''' ESCREVE O ARQUIVO TXT E APAGA TUDO QUE HAVIA '''
# with open('valores_celulares.txt', 'w') as arquivo: 
#     for valor in valores_celurares:
#         arquivo.write(f'{str(valor)}\n')


''' ACRESENTA CONTEUDO AO ARQUVI TXT '''
with open('valores_celulares.txt', 'a') as arquivo: 
    for valor in valores_celurares:
        arquivo.write(f'{str(valor)}\n')


''' LER ARQUVO TXT '''
# with open('valores_celulares.txt', 'r') as arquivo: 
#     for valor in arquivo:
#         print(valor)


''' LER E CASO PRECISO ESCREVER '''
# with open('valores_celulares.txt', 'r+') as arquivo: 
#     for valor in arquivo:
#         print(valor)
#     arquivo.write(str(input('Digite um valor: ') + '\n'))