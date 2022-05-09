v1 =  float(input('QUAL O SEU SALARIO R$1234.56: R$'))

if v1 <= 1250:
    print('SEU SALARIO TERA UM ALMENTO DE 15%')
    print(f'SEU SALARIO FINAL SERA DE R${((v1 * 15) / 100) + v1:.2f}')
else:
    print('SEU SALARIO TERA UM ALMENTO DE 10%')
    print(f'SEU SALARIO  FINAL SERA DE {((v1 * 10) / 100) + v1:.2f}')
