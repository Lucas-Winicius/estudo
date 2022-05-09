def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('HOUVE UM ERRO NA CRIAÇÃO DO ARQUIVO!')
    else:
        print(f'ARQUIVO {nome} CRIADO COM SUCESSO!')


def lerArquivo(nome):
    import ex115.lib.interface
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO ABRIR O ARQUIVO!')
    else:
        ex115.lib.interface.cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3}ANOS')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('HOUVE UM ERRO NA ABERTURA DO ARQUIVO!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('HOUVE UM ERRO AO ESCREVER OS DADOS')
        else:
            print(f'CADASTRO DE {nome} REALIZADO COM SUCESSO!')
            a.close()