from time import sleep

def criar_arquivo(nome_do_arquivo):
    with open(f'{nome_do_arquivo.lower()}.json', 'a+') as arquivo:
        sleep(1)

def salvar_json(nome_do_arquivo, *texto):
    nome_do_arquivo = nome_do_arquivo.lower()
    criar_arquivo(nome_do_arquivo)
    conteudo = ''

    for d in texto:
        conteudo += d.replace("'", '"')
    

    with open(f'{nome_do_arquivo}.json', 'w') as arquivo: 
        arquivo.write(conteudo)
        print('Texto Atualizado!')

def ler_json(nome_do_arquivo):
    nome_do_arquivo = nome_do_arquivo.lower()
    criar_arquivo(nome_do_arquivo)
    

    texto = ''

    with open(f'{nome_do_arquivo}.txt', 'r') as arquivo:
        for palavras in arquivo:
            texto += f'{palavras} '

    return texto
