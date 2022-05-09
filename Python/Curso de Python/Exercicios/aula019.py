estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('UNIDADE FEDERATIVA: ')).strip().capitalize()
    estado['sigla'] = str(input('SIGLA: ')).strip().upper()
    brasil.append(estado.copy())
for e in brasil:
    for k in e.values():
        print(k, end=' ')