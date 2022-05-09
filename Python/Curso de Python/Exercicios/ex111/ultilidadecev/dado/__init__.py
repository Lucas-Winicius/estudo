def leiaDinheiro(v):
    while True:
        valor = v.replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mERRO: "{v}" É UM PREÇO INVALIDO!\033[m')
            v = str(input('DIGITE O PREÇO: '))
        else:
            return float(valor)


def leiaint(txt):
    from time import sleep
    while True:
        valor = str(input(txt)).strip()
        if valor.isnumeric():
            print('\033[0;33mAGUARDE...\033[m')
            sleep(1.3)
            return int(valor)
            break
        else:
            print('\033[0;31mERRO: DIGITE UM VALOR INTEIRO VALIDO!\033[m')


def leiafloat():
    while True:
        try:
            valor = str(input('DIGITE UM VALOR REAL: '))
        except KeyboardInterrupt:
            print('\033[0;31mAÇAO INTERROMPIDA PELO USUARIO!\033[m')
            return 0
            break
        else:
            if '.' in valor:
                print('\033[0;33mPROCESSANDO INFORMAÇÕES...\033[m')
                return float(valor)
                break
            else:
                print('\033[0;31mERRO! PORFAVOR DIGITE UM NUMERO REAL VALIDO\033[m')