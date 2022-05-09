def factorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


n = int(input('DIGITE UM NUMERO: '))
print(f'O FACTORIAL DE {n} E IGUAL A {factorial(n)}')

f1 = factorial(5)
f2 = factorial(4)
f3 = factorial()
print(f'OS RESULTADOS FORAM {f1}, {f2}, {f3}')
