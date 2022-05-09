v1 =  str(input('DIGITE UMA FRASE: ')).upper().strip()

print(f'A LETRA *A* APARECE {v1.count("A")} VEZES NESSA FRASE')
print(f'A PRIMEIRA LETRA *A* APARECE NA POSIÇAO {v1.find("A")+1}')
print(f'A ULTIMA LETRA *A* APARECE NA POSICAO {v1.rfind("A")+1}')
