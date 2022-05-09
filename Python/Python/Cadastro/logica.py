from time import sleep


def ler_int(txt, er='Carregando...'):
    from time import sleep
    while True:
        v = str(input(txt))

        if v.isnumeric():
            sleep(1)
            print(er)
            return int(v)
            break

        if v.strip() == '':
            print('Valores vazios não são aceitos')
        
        else:
            print('Erro!')
    

def criar_arquivo():
    with open('Arquivos.txt', 'a+') as arquivo:
        sleep(1)



def cadastrar():
    criar_arquivo()
    user = str(input('Digite o nome de usuario: '))
    senha = str(input('Digite sua senha: '))

    with open('Arquivos.txt', 'a') as arquivo: 
        arquivo.write(f'{user};{senha}\n')
        print('Cadastro realizado!')

def cadastrar_extr(usuario, senha):
    criar_arquivo()
    user = usuario
    senha1 = senha

    with open('Arquivos.txt', 'a') as arquivo: 
        arquivo.write(f'{user};{senha1}\n')
        print('Cadastro realizado!')


def ver_user(msg=False):
    if msg:
        print('Verificando todos os usuarios...')
        print()
    todos = []
    criar_arquivo()
    with open('Arquivos.txt', 'r') as arquivo:
        for nomes in arquivo:
            nomes = nomes.replace(';', ' - ')
            usuario = ''
            for n1 in nomes:
                if n1 != ' ':
                    usuario = usuario + n1
                else:
                    todos.append(usuario)
                    break
        return todos


def user_ext(usr):
    todos = []
    criar_arquivo()
    with open('Arquivos.txt', 'r') as arquivo:
        for nomes in arquivo:
            nomes = nomes.replace(';', ' - ')
            usuario = ''
            for n1 in nomes:
                if n1 != ' ':
                    usuario = usuario + n1
                else:
                    if usr == usuario:
                        return True
                        break
                    else:
                        todos.append(usuario)
                        break
