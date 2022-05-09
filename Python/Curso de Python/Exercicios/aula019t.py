#DECLARAÇAO DE DICIONARIOS
dados = dict()
dados = { 'nome':'Pedro', 'idade':25 }

# ESCREVER OS INDICES
print(dados['nome']) # Pedro
print(dados['idade']) # 25

# ADICIONANDO ELEMENTOS
dados['sexo'] = 'M'

# REMOVER ELEMENTOS
del dados['idade']

filme = {'titulo':'Star Wars',
         'ano':1977,
         'diretor':'George lucas'
        }

# RETORNO DE VALORES
print(filme.values()) #RETORNO ** 'Star Wars', 1977, 'George lucas' **
print(filme.keys()) #RETORNO ** 'titulo', 'ano', 'diretor' **
print(filme.items()) #RETORNO ** ('titulo', 'Star Wars'), ('ano', 1977), ('diretor', 'George lucas') **

#RETORNAR VALORES E CHAVES
for key, valor in filme.items():
    print(f'O {key} É {valor}')

# PRATICA 01
'''pessoas = {'Nome':'', 'Sexo':'M', 'Idade':22}
print(f'O {pessoas["nome"]} TEM {pessoas["idade"]} ANOS')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
pessoas['Nome'] = str(input('DIGITE O SEU NOME: ')).strip().title()
for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

# PRATICA 02
'''brasil = list()
estado1 = {'uf':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'uf':'São Paulo', 'sigla':'SP'}

brasil.append(estado1)
brasil.append(estado2)
print(brasil[0]['uf'])'''

