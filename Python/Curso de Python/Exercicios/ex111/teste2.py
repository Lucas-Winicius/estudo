from ex111.ultilidadecev import moeda
from ex111.ultilidadecev import dado

p = str(input('DIGITE O PREÇO: ')).strip()
# d = int(input('DIGITE O AUMENTO: [%] '))
# r = int(input('DIGITE A REDUÇÃO: [%] '))
moeda.resumo(dado.leiaDinheiro(p), 10, 10)
