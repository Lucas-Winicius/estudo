palavras = 'APRENDER', 'PROGRAMAR', \
            'LINGUAGEM', 'PYTHON', \
            'CURSO', 'GRATIS', \
            'ESTUDAR', 'PRATICAR', \
            'TRABALHAR', 'MERCADO', \
            'PROGRAMADOR', 'FUTURO'

for p in palavras:
         print(f'\nNA PALAVRA {p.lower()} TEMOS ', end='')
         for letra in p:
             if letra.lower() in 'aeiou':
                 print(letra.lower(), end=' ')