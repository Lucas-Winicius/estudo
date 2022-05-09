produtos = ["ABC123", "abd012", " ABS111", "AbB222"]

texto = "abd012"

def tratar(texto):
    tratados = list()
    for palavras in texto:
        palavras = palavras.upper()
        palavras = palavras.strip()
        tratados.append(palavras)
    return tratados

print(tratar(produtos))