p1 = input('DIGITE ALGO: ')

print(' ')
print('-=--=--=--=--=--=--=--=--=-')
print('*True* E IGUAL A "SIM"')
print('*False* E IGUAL A "NÃO" ')
print('-=--=--=--=--=--=--=--=--=-')
print(' ')
print('O TIPO PRIMITIVO DESSE VALOR E ', p1.__class__)
print('SO TEM ESPAÇOS? ', p1.isspace( ))
print('E UM NUMERO? ', p1.isnumeric())
print('E UM ALFABETICO? ', p1.isalpha())
print('E ALFANUMERICO?', p1.isnumeric())
print('ESTA EM MAIUSCULAS?',p1.isupper())
print('ESTA EM MINUSCULAS?', p1.islower())
print('ESTA CAPTALIZADA?', p1.istitle())
