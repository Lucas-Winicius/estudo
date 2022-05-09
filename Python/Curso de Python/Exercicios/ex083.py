list = []
r = 0

list.append(input('DIGITE SUA EXPRESSAO: '))

while True:
    if '(' in list:
        list.remove('(')
        r += 1
    elif ')' in list:
        list.remove(')')
        r += 1
    else:
        break
if r % 2 == 0:
    print('SUA EXPRESSAO ESTA VALIDA!')
else:
    print('SUA EXPRESSAO ESTA ERRADA!')
