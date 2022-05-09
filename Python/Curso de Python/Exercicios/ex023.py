v1 = int(input('DIGITE UM NUMERO: '))

u = v1 // 1 % 10
d = v1 // 10 % 10
c = v1 // 100 % 10
m = v1 // 1000 % 10

print(f'ANALIZANDO O NUMERO {v1}...')

print(f'UNIDADE: {u}')
print(f'DEZENA: {d}')
print(f'CENTENA: {c}')
print(f'MILHAR: {m}')
