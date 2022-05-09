from datetime import date
from time import sleep

v1 = int(input('QUE ANO VOCE QUER ANALIZAR? CASO ESTEJA EM UMA CAVERNA E NAO SAIBA DIGITE 0: '))
print('AGUARDE PRECISO FAZER CONTAS MATEMATICAS QUE NAO EO MEU FORTE')
sleep(2)

if v1 == 0:
    v1 = date.today().year
    print(f'OLHA NEANDERTAL VOCE ESTA NO ANO DE {v1} ')

if v1 >= 2050:
    print('CYBERPUNCK')

if v1 % 4:
    print(f'O ANO DE {v1} E *BISSEXTO*')
else:
    print(f'o ano de {v1}  nao e bissexto')
    print('SERA Q O FIM DO MUNDO ETA PROXIMO?')
