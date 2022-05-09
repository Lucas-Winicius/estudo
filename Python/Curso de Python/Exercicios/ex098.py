from time import sleep

def conno(f, i, p):
    for c in range(f, i + 1, p):
        print(c, end=' ')
        sleep(1)
    print('FIM')


def conre(i, f, p):
    for c in range(i, f - 1, p):
        print(c, end=' ')
        sleep(1)
    print('FIM')



print('-='*35)
print('CONTAGEM DE 1 ATE 10  DE 1 EM 1')
for c in range(1, 11):
    print(c, end=' ')
    sleep(1)
print('FIM')
print('-='*35)
print('CONTAGEM DE 10 ATE 0 DE 2 EM 2')
for c in range(10, -1, -2):
    print(c, end=' ')
    sleep(1)
print('FIM')
print('-='*35)
print('AGORA EA SUA VEZ!')
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
print('-='*35)
print(f'CONTAGEM DE {i} ATE {f} DE {p} EM {p}')

conno(f, i, p)
conre(i, f, p)
