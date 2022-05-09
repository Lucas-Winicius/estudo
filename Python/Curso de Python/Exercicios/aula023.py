try:
    a = int(input('NUMERADOR: '))
    b = int(input('DENOMINADOR: '))
    r = a / b
except {ValueError, TypeError}:
    print('TIVEMOS UM POBLEMA COM O TIPO DE DADOS QUE VOCE DIGITOU')

except ZeroDivisionError:
    print('UM NUMERO NAO PODE SER DIVIDIDO POR 0!')

except KeyboardInterrupt:
    print('VOCE PREFERIU NAO INFORMAR OS DADOS!')

else:
    print(f'O RESULTADO É {r:.1f}')

finally:
    print('VOLTE SEMPRE')