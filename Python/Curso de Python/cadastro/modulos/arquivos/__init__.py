def valor(txt):
    while True:
        try:
            v = int(input(txt))
        except:
            print('HOUVE UM ERRO AO ANALIZAR O VALOR DIGITADO')
        else:
            return v
            break


def form(txt):
    texto = txt.strip().title
    return texto